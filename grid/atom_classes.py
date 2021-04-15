from typing import NamedTuple
import clingo


class TicksPerBeatAtom(NamedTuple):
    ticks_per_beat: int


class StressAtom(NamedTuple):
    bar: int
    beat: int
    stress: str


class GridAtom(NamedTuple):
    bar: int
    beat: int
    numerator: int
    denominator: int


class GridTicksAtom(NamedTuple):
    bar: int
    beat: int
    numerator: int
    denominator: int
    grid_ticks: int


class EndTicksAtom(NamedTuple):
    end_ticks: int


class GridOrderAtom(NamedTuple):
    bar: int
    beat: int
    numerator: int
    denominator: int
    grid_number: int


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
        symbol.name == 'ticks_per_beat' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return TicksPerBeatAtom(
            ticks_per_beat=symbol.arguments[0].number
        )

    if (
        symbol.name == 'stress' and
        len(symbol.arguments) == 3 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number and
        symbol.arguments[2].type == clingo.SymbolType.String
    ):
        return StressAtom(
            bar=symbol.arguments[0].number,
            beat=symbol.arguments[1].number,
            stress=symbol.arguments[2].string
        )

    if (
        symbol.name == 'grid' and
        len(symbol.arguments) == 4 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number and
        symbol.arguments[2].type == clingo.SymbolType.Number and
        symbol.arguments[3].type == clingo.SymbolType.Number
    ):
        return GridAtom(
            bar=symbol.arguments[0].number,
            beat=symbol.arguments[1].number,
            numerator=symbol.arguments[2].number,
            denominator=symbol.arguments[3].number
        )

    if (
        symbol.name == 'grid_ticks' and
        len(symbol.arguments) == 5 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number and
        symbol.arguments[2].type == clingo.SymbolType.Number and
        symbol.arguments[3].type == clingo.SymbolType.Number and
        symbol.arguments[4].type == clingo.SymbolType.Number
    ):
        return GridTicksAtom(
            bar=symbol.arguments[0].number,
            beat=symbol.arguments[1].number,
            numerator=symbol.arguments[2].number,
            denominator=symbol.arguments[3].number,
            grid_ticks=symbol.arguments[4].number
        )

    if (
        symbol.name == 'end_ticks' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return EndTicksAtom(
            end_ticks=symbol.arguments[0].number
        )

    if (
        symbol.name == 'grid_order' and
        len(symbol.arguments) == 5 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number and
        symbol.arguments[2].type == clingo.SymbolType.Number and
        symbol.arguments[3].type == clingo.SymbolType.Number and
        symbol.arguments[4].type == clingo.SymbolType.Number
    ):
        return GridOrderAtom(
            bar=symbol.arguments[0].number,
            beat=symbol.arguments[1].number,
            numerator=symbol.arguments[2].number,
            denominator=symbol.arguments[3].number,
            grid_number=symbol.arguments[4].number
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
        symbol.name == 'ticks_per_beat' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'ticks_per_beat({symbol.arguments[0].number}).'

    if (
        symbol.name == 'stress' and
        len(symbol.arguments) == 3 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number and
        symbol.arguments[2].type == clingo.SymbolType.String
    ):
        return f'stress({symbol.arguments[0].number},{symbol.arguments[1].number},"{symbol.arguments[2].string}").'

    if (
        symbol.name == 'grid' and
        len(symbol.arguments) == 4 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number and
        symbol.arguments[2].type == clingo.SymbolType.Number and
        symbol.arguments[3].type == clingo.SymbolType.Number
    ):
        return f'grid({symbol.arguments[0].number},{symbol.arguments[1].number},{symbol.arguments[2].number},{symbol.arguments[3].number}).'

    if (
        symbol.name == 'grid_ticks' and
        len(symbol.arguments) == 5 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number and
        symbol.arguments[2].type == clingo.SymbolType.Number and
        symbol.arguments[3].type == clingo.SymbolType.Number and
        symbol.arguments[4].type == clingo.SymbolType.Number
    ):
        return f'grid_ticks({symbol.arguments[0].number},{symbol.arguments[1].number},{symbol.arguments[2].number},{symbol.arguments[3].number},{symbol.arguments[4].number}).'

    if (
        symbol.name == 'end_ticks' and
        len(symbol.arguments) == 1 and
        symbol.arguments[0].type == clingo.SymbolType.Number
    ):
        return f'end_ticks({symbol.arguments[0].number}).'

    if (
        symbol.name == 'grid_order' and
        len(symbol.arguments) == 5 and
        symbol.arguments[0].type == clingo.SymbolType.Number and
        symbol.arguments[1].type == clingo.SymbolType.Number and
        symbol.arguments[2].type == clingo.SymbolType.Number and
        symbol.arguments[3].type == clingo.SymbolType.Number and
        symbol.arguments[4].type == clingo.SymbolType.Number
    ):
        return f'grid_order({symbol.arguments[0].number},{symbol.arguments[1].number},{symbol.arguments[2].number},{symbol.arguments[3].number},{symbol.arguments[4].number}).'

    return None
