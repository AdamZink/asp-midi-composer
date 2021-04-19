# ASP MIDI Composer

Generate MIDI music with answer set programming.

## Requirements

### Dependencies

Requires python3 with `midiutil` and `clingo` modules installed.

### Input

Prepare a JSON config file such as `config_4_bars.json`:
```json
{
  "grid": {
    "bars": 4,
    "beatsPerBar": 4,
    "constraints": [
      "use_numbered_beats",
      "use_grid(*,2,1,2)"
    ]
  },
  "notes": {
    "constraints": [
      "no_consecutive_pitches",
      "no_large_intervals"
    ]
  }
}
```

## Build parser modules

```commandline
make atom_classes
```
* Generates two files:
  * `grid/atom_classes.py` (to parse ASP results from `generate_grid.py`)
  * `notes/atom_classes.py` (to parse ASP results from `generate_notes.py`)

## Generate MIDI file

```commandline
python3 compose.py --config-path=config_4_bars.json
```
* MIDI file is written to `output/`
