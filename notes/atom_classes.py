from typing import NamedTuple
import clingo


class BarsAtom(NamedTuple):
    bars: int


class TicksPerBeatAtom(NamedTuple):
    ticks_per_beat: int


class MinPitchAtom(NamedTuple):
    min_pitch: int


class KeyRootPitchAtom(NamedTuple):
    key_root_pitch: int


class MaxPitchAtom(NamedTuple):
    max_pitch: int


class NoteNumberAtom(NamedTuple):
    grid_number: int


class NoteTicksStartAtom(NamedTuple):
    grid_number: int
    start__grid__ticks: int


class NoteTicksDurationAtom(NamedTuple):
    grid_number: int
    ticks__duration: int


class NoteStressAtom(NamedTuple):
    grid_number: int
    stress: str


class NotePitchAtom(NamedTuple):
    grid_number: int
    pitch: int


def get_class_map(symbols):
    class_map = {}
    for symbol in symbols:
        class_object = get_class(symbol)
        if class_object is not None:
            if symbol.name not in class_map:
                class_map[symbol.name] = []
            class_map[symbol.name].append(class_object)
    return class_map


def get_class(symbol):
    if (
        symbol.name == 'bars' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return BarsAtom(
            bars=symbol.arguments[0].number
        )

    if (
        symbol.name == 'ticks_per_beat' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return TicksPerBeatAtom(
            ticks_per_beat=symbol.arguments[0].number
        )

    if (
        symbol.name == 'min_pitch' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return MinPitchAtom(
            min_pitch=symbol.arguments[0].number
        )

    if (
        symbol.name == 'key_root_pitch' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return KeyRootPitchAtom(
            key_root_pitch=symbol.arguments[0].number
        )

    if (
        symbol.name == 'max_pitch' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return MaxPitchAtom(
            max_pitch=symbol.arguments[0].number
        )

    if (
        symbol.name == 'note_number' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return NoteNumberAtom(
            grid_number=symbol.arguments[0].number
        )

    if (
        symbol.name == 'note_ticks_start' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return NoteTicksStartAtom(
            grid_number=symbol.arguments[0].number,
            start__grid__ticks=symbol.arguments[1].number
        )

    if (
        symbol.name == 'note_ticks_duration' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return NoteTicksDurationAtom(
            grid_number=symbol.arguments[0].number,
            ticks__duration=symbol.arguments[1].number
        )

    if (
        symbol.name == 'note_stress' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.String
    ):
        return NoteStressAtom(
            grid_number=symbol.arguments[0].number,
            stress=symbol.arguments[1].string
        )

    if (
        symbol.name == 'note_pitch' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return NotePitchAtom(
            grid_number=symbol.arguments[0].number,
            pitch=symbol.arguments[1].number
        )


def get_atom_map(symbols):
    atom_map = {}
    for symbol in symbols:
        atom_string = get_atom(symbol)
        if atom_string is not None:
            if symbol.name not in atom_map:
                atom_map[symbol.name] = []
            atom_map[symbol.name].append(atom_string)
    return atom_map


def get_atom(symbol):
    if (
        symbol.name == 'bars' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'bars({symbol.arguments[0].number}).'

    if (
        symbol.name == 'ticks_per_beat' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'ticks_per_beat({symbol.arguments[0].number}).'

    if (
        symbol.name == 'min_pitch' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'min_pitch({symbol.arguments[0].number}).'

    if (
        symbol.name == 'key_root_pitch' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'key_root_pitch({symbol.arguments[0].number}).'

    if (
        symbol.name == 'max_pitch' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'max_pitch({symbol.arguments[0].number}).'

    if (
        symbol.name == 'note_number' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'note_number({symbol.arguments[0].number}).'

    if (
        symbol.name == 'note_ticks_start' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return f'note_ticks_start({symbol.arguments[0].number},{symbol.arguments[1].number}).'

    if (
        symbol.name == 'note_ticks_duration' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return f'note_ticks_duration({symbol.arguments[0].number},{symbol.arguments[1].number}).'

    if (
        symbol.name == 'note_stress' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.String
    ):
        return f'note_stress({symbol.arguments[0].number},"{symbol.arguments[1].string}").'

    if (
        symbol.name == 'note_pitch' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return f'note_pitch({symbol.arguments[0].number},{symbol.arguments[1].number}).'

    return None
