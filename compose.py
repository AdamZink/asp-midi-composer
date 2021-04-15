import json
from midiutil import MIDIFile
from grid.generate_grid import get_grid
from notes.generate_notes import get_notes
import argparse


parser = argparse.ArgumentParser(description='Generate MIDI music')
parser.add_argument('--config-path', help='Path to config file with desired MIDI properties')

args = parser.parse_args()
assert args.config_path and len(args.config_path) > 0

stress_velocity_map = {
    'stressed': 88,
    'slightly stressed': 78,
    'unstressed': 72
}


def get_config_json(config_path):
    with open(config_path, 'r') as f:
        return json.loads(f.read())


config_json = get_config_json(args.config_path)

print(f'Config properties:\n{json.dumps(config_json, indent=2)}')

grid_atom_map = get_grid(config_json)
print(grid_atom_map)

fact_list_for_notes = []
for _, atom_list in grid_atom_map.items():
    fact_list_for_notes.extend(atom_list)

notes_class_map = get_notes(config_json, fact_list_for_notes)
print(notes_class_map)


assert 'ticks_per_beat' in notes_class_map and len(notes_class_map['ticks_per_beat']) == 1
assert 'note_number' in notes_class_map and len(notes_class_map['note_number']) > 0
assert 'note_ticks_start' in notes_class_map and len(notes_class_map['note_ticks_start']) == len(notes_class_map['note_number'])
assert 'note_ticks_duration' in notes_class_map and len(notes_class_map['note_ticks_duration']) == len(notes_class_map['note_number'])
assert 'note_stress' in notes_class_map and len(notes_class_map['note_stress']) == len(notes_class_map['note_number'])
assert 'note_pitch' in notes_class_map and len(notes_class_map['note_pitch']) == len(notes_class_map['note_number'])

ticks_per_beat: int = notes_class_map['ticks_per_beat'][0].ticks_per_beat
note_number_list = [x.grid_number for x in notes_class_map['note_number']]
note_ticks_start_map = {x.grid_number: x.start__grid__ticks for x in notes_class_map['note_ticks_start']}
note_ticks_duration_map = {x.grid_number: x.ticks__duration for x in notes_class_map['note_ticks_duration']}
note_stress_map = {x.grid_number: x.stress for x in notes_class_map['note_stress']}
note_pitch_map = {x.grid_number: x.pitch for x in notes_class_map['note_pitch']}

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

output_path = f'output/test-{args.config_path.replace(".json","")}.mid'
with open(output_path, 'wb') as output_file:
    MyMIDI.writeFile(output_file)

print(f'Wrote {output_path}')
