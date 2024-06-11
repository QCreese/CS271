# hack_parser.py

# C-instruction tables
# These tables map the parts of the C-instruction to their binary codes
DEST_TABLE = {
    None: '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
    'AM': '101', 'AD': '110', 'AMD': '111'
}

COMP_TABLE = {
    '0': '0101010', '1': '0111111', '-1': '0111010',
    'D': '0001100', 'A': '0110000', '!D': '0001101',
    '!A': '0110001', '-D': '0001111', '-A': '0110011',
    'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110',
    'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011',
    'A-D': '0000111', 'D&A': '0000000', 'D|A': '0010101',
    'M': '1110000', '!M': '1110001', '-M': '1110011',
    'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010',
    'D-M': '1010011', 'M-D': '1000111', 'D&M': '1000000',
    'D|M': '1010101'
}

JUMP_TABLE = {
    None: '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
    'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'
}

# Helper function to convert a decimal number to a 15-bit binary string
def decimal_to_binary(value):
    return f"{value:015b}"

# Function to parse a line of assembly code and return its binary representation
def parse_line(line, symbol_table, variable_address):
    line = line.split('//')[0].strip()  # Remove comments and trim whitespace
    if not line or line.startswith('('):  # Ignore empty lines and labels
        return None

    if line.startswith('@'):  # A-instruction
        symbol = line[1:]
        if symbol.isdigit():
            address = int(symbol)
        else:
            if symbol not in symbol_table:  # Add new variables to the symbol table
                symbol_table[symbol] = variable_address[0]
                variable_address[0] += 1
            address = symbol_table[symbol]
        return '0' + decimal_to_binary(address)
    else:  # C-instruction
        dest, comp, jump = None, None, None
        if '=' in line:
            dest, line = line.split('=')
        if ';' in line:
            comp, jump = line.split(';')
        else:
            comp = line
        dest_code = DEST_TABLE[dest]
        comp_code = COMP_TABLE[comp]
        jump_code = JUMP_TABLE[jump]
        return '111' + comp_code + dest_code + jump_code

