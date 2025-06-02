import sys
import pickle
from ops import OPCODES, MNEMONICS, sta24
from memory import zero_memory_map, dump_memory, MEMORY_SIZE


def get_lines(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(";"):
                continue
            if line == "":
                continue
            line = line.split(";")[0].strip()
            lines.append(line)

    return lines


def assemble(source_lines):
    addr = 0x00
    memory = zero_memory_map(MEMORY_SIZE)
    labels = {}
    unresolved = []

    # First pass: collect labels and resolve addresses
    for line in source_lines:
        if line.endswith(":"):
            labels[line[:-1]] = addr
        else:
            addr += 4

    # Second pass: assemble instructions
    addr = 0x00
    for line in source_lines:
        if line.endswith(":"):
            continue

        parts = line.split(" ")
        instruction = parts[0].upper()
        operand = parts[1] if len(parts) > 1 else 0

        opcode = MNEMONICS.get(instruction)
        if opcode is None:
            if instruction.startswith("0X"):
                memory = sta24(memory, addr, int(instruction, 16))
            else:
                raise ValueError(f"Unknown instruction: {instruction}")
        if opcode is not None:
            memory[addr] = opcode
            if operand != 0:
                operand_val = labels.get(operand)
                if operand_val is None:
                    raise ValueError(f"Unknown operand: {operand}")
                memory = sta24(memory, addr + 1, operand_val)
        addr += 4
    return memory


if __name__ == "__main__":
    file_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output.bin"
    lines = get_lines(file_path)
    memory = assemble(lines)
    # dump_memory(memory)
    with open(output_path, "wb") as f:
        pickle.dump(memory, f)
