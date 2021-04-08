import clingo
from midiutil import MIDIFile
from atom_classes import *


prg = clingo.Control()
prg.configuration.solve.models = 1

with open('compose.lp', 'r') as f:
    prg.add('base', [], f.read())

prg.ground([('base', [])])


# TODO formula to convert MIDI pitch number to frequency
pitch_frequency_map = {
    '60': 261.626,
    '62': 293.665,
    '64': 329.628,
    '65': 349.228,
    '67': 391.995
}

stress_velocity_map = {
    'stressed': 86,
    'slightly stressed': 83,
    'unstressed': 80
}


def on_model(m):
    model_count = m.number
    atom_map = get_class_map(m.symbols(atoms=True))

    assert 'ticks_per_beat' in atom_map and len(atom_map['ticks_per_beat']) == 1
    assert 'note_number' in atom_map and len(atom_map['note_number']) > 0
    assert 'note_ticks_start' in atom_map and len(atom_map['note_ticks_start']) == len(atom_map['note_number'])
    assert 'note_ticks_duration' in atom_map and len(atom_map['note_ticks_duration']) == len(atom_map['note_number'])
    assert 'note_stress' in atom_map and len(atom_map['note_stress']) == len(atom_map['note_number'])
    assert 'note_pitch' in atom_map and len(atom_map['note_pitch']) == len(atom_map['note_number'])

    ticks_per_beat: int = atom_map['ticks_per_beat'][0].ticks_per_beat
    note_number_list = [x.grid_number for x in atom_map['note_number']]
    note_ticks_start_map = {x.grid_number: x.start__grid__ticks for x in atom_map['note_ticks_start']}
    note_ticks_duration_map = {x.grid_number: x.ticks__duration for x in atom_map['note_ticks_duration']}
    note_stress_map = {x.grid_number: x.stress for x in atom_map['note_stress']}
    note_pitch_map = {x.grid_number: x.pitch for x in atom_map['note_pitch']}

    # Write MIDI file
    tempo = 80  # In BPM

    MyMIDI = MIDIFile(
        numTracks=1,
        ticks_per_quarternote=ticks_per_beat,
        eventtime_is_ticks=True
    )

    MyMIDI.addTempo(0, 0, tempo)

    for note_number in sorted(note_number_list):
        if note_pitch_map[note_number] > 0:
            MyMIDI.addNote(
                0, 0,
                note_pitch_map[note_number],
                note_ticks_start_map[note_number],
                note_ticks_duration_map[note_number],
                stress_velocity_map[note_stress_map[note_number]]
            )

    with open(f'../output/test_{model_count}.mid', 'wb') as output_file:
        MyMIDI.writeFile(output_file)


prg.solve(on_model=on_model)
