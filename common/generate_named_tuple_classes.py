import clingo
import json
import re
import argparse


parser = argparse.ArgumentParser(description='Generate named tuple classes')
parser.add_argument('--defs-path', help='Input path of defs.lp file')
parser.add_argument('--output-path', help='Output path for the named tuple classes')

args = parser.parse_args()
assert args.defs_path and len(args.defs_path) > 0
assert args.output_path and len(args.output_path) > 0


# Property values
ARITY = 'arity'
DESCRIPTION = 'description'
NAME = 'name'
TYPE = 'type'

PREDICATE_NUMBER_PROPERTIES = [ARITY]
PREDICATE_STRING_PROPERTIES = [DESCRIPTION]

TERM_STRING_PROPERTIES = [NAME, TYPE]

python_data_type_map = {
    'Number': 'int',
    'String': 'str'
}

clingo_type_map = {
    'Number': 'number',
    'String': 'string'
}


class DefsParser:

    def __init__(self, defs_path: str, output_path: str):
        self.definition_map = {}
        self.defs_path = defs_path
        self.output_path = output_path

    def parse_def_predicate(self, symbol):
        assert symbol.arguments[0].type == clingo.SymbolType.String
        predicate_name = symbol.arguments[0].string

        assert symbol.arguments[1].type == clingo.SymbolType.String
        property_key = symbol.arguments[1].string

        if predicate_name not in self.definition_map:
            self.definition_map[predicate_name] = {
                'terms': {}
            }

        value_symbol = symbol.arguments[2]

        if property_key in PREDICATE_NUMBER_PROPERTIES:
            assert value_symbol.type == clingo.SymbolType.Number
            self.definition_map[predicate_name][property_key] = value_symbol.number

        elif property_key in PREDICATE_STRING_PROPERTIES:
            assert value_symbol.type == clingo.SymbolType.String
            self.definition_map[predicate_name][property_key] = value_symbol.string

    def parse_def_term(self, symbol):
        assert symbol.arguments[0].type == clingo.SymbolType.String
        predicate_name = symbol.arguments[0].string

        assert symbol.arguments[1].type == clingo.SymbolType.Number
        term_number_as_string = str(symbol.arguments[1].number)

        assert symbol.arguments[2].type == clingo.SymbolType.String
        property_key = symbol.arguments[2].string

        if predicate_name not in self.definition_map:
            self.definition_map[predicate_name] = {
                'terms': {}
            }

        if term_number_as_string not in self.definition_map[predicate_name]['terms']:
            self.definition_map[predicate_name]['terms'][term_number_as_string] = {}

        value_symbol = symbol.arguments[3]

        if property_key in TERM_STRING_PROPERTIES:
            assert value_symbol.type == clingo.SymbolType.String
            self.definition_map[predicate_name]['terms'][term_number_as_string][property_key] = value_symbol.string

    def generate_named_tuple_classes(self):
        ctl = clingo.Control()
        ctl.configuration.solve.models = 1

        print(f'Generating classes from {self.defs_path}...')
        with open(self.defs_path, 'r') as f:
            ctl.add('base', [], f.read())

        ctl.ground([('base', [])])

        with ctl.solve(yield_=True) as handle:
            models = [m for m in handle]
            assert len(models) == 1
            for model in models:
                for symbol in model.symbols(atoms=True):
                    if symbol.name == 'def_predicate' and len(symbol.arguments) == 3:
                        self.parse_def_predicate(symbol)
                    elif symbol.name == 'def_term' and len(symbol.arguments) == 4:
                        self.parse_def_term(symbol)
                    else:
                        print(f"Warning: unexpected symbol {symbol.name}/{len(symbol.arguments)}")

        #print(json.dumps(self.definition_map, indent=2))

        class_lines = []
        class_parser_lines = []
        atom_parser_lines = []

        for predicate_name, predicate_properties in self.definition_map.items():
            parser_if_lines = []
            class_parser_then_lines = []
            atom_parser_then_line_parts = []

            capitalized_tokens = [token.capitalize() for token in predicate_name.split('_')]
            class_name = ''.join(capitalized_tokens + ['Atom'])
            class_lines.append(f'\n\nclass {class_name}(NamedTuple):\n')

            assert ARITY in predicate_properties
            arity = predicate_properties[ARITY]
            parser_if_lines.append("if (\n")
            parser_if_lines.append(f"    symbol.name == '{predicate_name}' and\n")
            parser_if_lines.append(f"    len(symbol.arguments) == {arity} and\n")

            class_parser_then_lines.append(f"    return {class_name}(\n")
            atom_parser_then_line_parts.append(f"    return f'{predicate_name}(")

            assert len(predicate_properties['terms']) > 0
            term_tuples = [(term_number_as_string, term_properties) for term_number_as_string, term_properties in predicate_properties['terms'].items()]
            arg_number = 0
            for term_tuple in sorted(term_tuples, key=lambda t: int(t[0])):
                assert NAME in term_tuple[1]
                assert TYPE in term_tuple[1]
                variable_tokens = re.sub(r'([A-Z])', r' \1', term_tuple[1][NAME]).split()
                variable_name = '_'.join([token.lower() for token in variable_tokens])
                variable_type = term_tuple[1][TYPE]
                class_lines.append(f"    {variable_name}: {python_data_type_map[variable_type]}\n")

                space_and = ' and' if arg_number + 1 < arity else ''
                parser_if_lines.append(f"    symbol.arguments[{arg_number}].type == clingo.SymbolType.{variable_type}{space_and}\n")

                comma = ',' if arg_number + 1 < arity else ''
                class_parser_then_lines.append(f"        {variable_name}=symbol.arguments[{arg_number}].{clingo_type_map[variable_type]}{comma}\n")
                double_quote = '"' if variable_type == "String" else ''
                atom_parser_then_line_parts.append(f"{double_quote}{{symbol.arguments{[arg_number]}.{clingo_type_map[variable_type]}}}{double_quote}{comma}")

                arg_number += 1

            parser_if_lines.append('):\n')
            class_parser_then_lines.append(f'    )\n\n')
            atom_parser_then_line_parts.append(f").'\n\n")

            class_parser_lines.extend(parser_if_lines)
            class_parser_lines.extend(class_parser_then_lines)
            atom_parser_lines.extend(parser_if_lines)
            atom_parser_lines.extend([''.join(atom_parser_then_line_parts)])

        print(f'Writing output classes to {self.output_path}...')
        with open(self.output_path, 'w') as f:
            f.write('from typing import NamedTuple\n')
            f.write('import clingo\n')

            for line in class_lines:
                f.write(line)

            f.write('''\n
def get_class_map(symbols):
    class_map = {}
    for symbol in symbols:
        class_object = get_class(symbol)
        if class_object is not None:
            if symbol.name not in class_map:
                class_map[symbol.name] = []
            class_map[symbol.name].append(class_object)
    return class_map\n''')

            f.write('\n\ndef get_class(symbol):\n')

            for line in class_parser_lines:
                f.write(f'    {line}')

            f.write('''
def get_atom_map(symbols):
    atom_map = {}
    for symbol in symbols:
        atom_string = get_atom(symbol)
        if atom_string is not None:
            if symbol.name not in atom_map:
                atom_map[symbol.name] = []
            atom_map[symbol.name].append(atom_string)
    return atom_map\n''')

            f.write('\n\ndef get_atom(symbol):\n')

            for line in atom_parser_lines:
                f.write(f'    {line}')

            f.write('    return None\n')


if __name__ == '__main__':
    defsParser = DefsParser(
        defs_path=args.defs_path,
        output_path=args.output_path
    )
    defsParser.generate_named_tuple_classes()
