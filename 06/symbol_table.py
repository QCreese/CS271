# symbol_table.py

# Predefined symbols and their corresponding addresses
PREDEFINED_SYMBOLS = {
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4,
    'SCREEN': 16384,
    'KBD': 24576,
}

# R0 to R15 registers
for i in range(16):
    PREDEFINED_SYMBOLS[f'R{i}'] = i

# Function to initialize the symbol table with predefined symbols
def initialize_symbol_table():
    return PREDEFINED_SYMBOLS.copy()

# First pass: process labels and build the initial symbol table
def first_pass(lines):
    symbol_table = initialize_symbol_table()
    rom_address = 0
    for line in lines:
        line = line.split('//')[0].strip()  # Remove comments and trim whitespace
        if line:
            if line.startswith('(') and line.endswith(')'):  # Label
                label = line[1:-1]
                symbol_table[label] = rom_address
            else:
                rom_address += 1  # Increase ROM address for each instruction
    return symbol_table


