from typing import NamedTuple
import clingo


class RhythmNumberAtom(NamedTuple):
    rhythm_number: int


class RhythmTicksStartAtom(NamedTuple):
    rhythm_number: int
    start__rhythm__ticks: int


class RhythmTicksDurationAtom(NamedTuple):
    rhythm_number: int
    ticks__duration: int


class RhythmStressAtom(NamedTuple):
    rhythm_number: int
    stress: str


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
        symbol.name == 'rhythm_number' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return RhythmNumberAtom(
            rhythm_number=symbol.arguments[0].number
        )

    if (
        symbol.name == 'rhythm_ticks_start' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return RhythmTicksStartAtom(
            rhythm_number=symbol.arguments[0].number,
            start__rhythm__ticks=symbol.arguments[1].number
        )

    if (
        symbol.name == 'rhythm_ticks_duration' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return RhythmTicksDurationAtom(
            rhythm_number=symbol.arguments[0].number,
            ticks__duration=symbol.arguments[1].number
        )

    if (
        symbol.name == 'rhythm_stress' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.String
    ):
        return RhythmStressAtom(
            rhythm_number=symbol.arguments[0].number,
            stress=symbol.arguments[1].string
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
        symbol.name == 'rhythm_number' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'rhythm_number({symbol.arguments[0].number}).'

    if (
        symbol.name == 'rhythm_ticks_start' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return f'rhythm_ticks_start({symbol.arguments[0].number},{symbol.arguments[1].number}).'

    if (
        symbol.name == 'rhythm_ticks_duration' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number
    ):
        return f'rhythm_ticks_duration({symbol.arguments[0].number},{symbol.arguments[1].number}).'

    if (
        symbol.name == 'rhythm_stress' and
        len(symbol.arguments) == 2 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.String
    ):
        return f'rhythm_stress({symbol.arguments[0].number},"{symbol.arguments[1].string}").'

    return None
