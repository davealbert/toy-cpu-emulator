import sys
import pickle
from app.instructions import mnemonic_map
from app.memory import MemoryManager
import os
import importlib


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
    memory = MemoryManager()
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

        opcode = mnemonic_map.get(instruction)
        if opcode is None:
            if instruction.startswith("0X"):
                memory.set_memory_le24(addr, int(instruction, 16))
            else:
                raise ValueError(f"Unknown instruction: {instruction}")
        if opcode is not None:
            memory.set_memory(addr, opcode)
            if operand != 0:
                if operand.startswith("0x"):
                    operand_val = int(operand, 16)
                else:
                    operand_val = labels.get(operand)
                if operand_val is None:
                    raise ValueError(f"Unknown operand: {operand}")
                memory.set_memory_le24(addr + 1, operand_val)
        addr += 4
    return memory

def load_all_instructions(debug=False):
    if debug:
        print("    Loading instructions...")
    instructions_path = os.path.join(os.path.dirname(__file__), "instructions")
    for filename in os.listdir(instructions_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = f"app.instructions.{filename[:-3]}"
            if debug:
                print(f"    Loading instruction: {filename[:-3]} ({module_name})")
            importlib.import_module(module_name)
    if debug:
        print("    Instructions loaded.\n")
        print(mnemonic_map)



if __name__ == "__main__":
    load_all_instructions(debug=True)
    file_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output.bin"
    lines = get_lines(file_path)
    memory = assemble(lines)
    memory.dump_memory(full=True)
    with open(output_path, "wb") as f:
        pickle.dump(memory.memory, f)
