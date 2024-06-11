# assembler.py

import sys
from hack_parser import parse_line  
from symbol_table import first_pass

# Main assembly function: convert assembly code to machine code
def assemble(assembly_code):
    lines = assembly_code.strip().split('\n')
    symbol_table = first_pass(lines)  # Build symbol table with labels
    variable_address = [16]  # Start allocating variables at address 16
    binary_code = []  # Renamed to avoid outer scope conflict

    for line in lines:
        binary_line = parse_line(line, symbol_table, variable_address)
        if binary_line:
            binary_code.append(binary_line)

    return '\n'.join(binary_code)

# Helper function to read assembly code from a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Specified encoding
        return file.read()

# Helper function to write machine code to a file
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:  # Specified encoding
        file.write(content)

if __name__ == "__main__":
    # Ensure the correct number of command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python assembler.py <input_file.asm> <output_file.hack>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read, assemble, and write the machine code
    asm_code_content = read_file(input_file)
    bin_code = assemble(asm_code_content)
    write_file(output_file, bin_code)

    print(f"Assembly complete. Output written to {output_file}")
