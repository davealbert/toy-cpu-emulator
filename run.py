import sys
import pickle
from memory import dump_memory
from ops import OPCODES, MNEMONICS, sta24, lda24

def run(memory):
    addr = 0x00
    acc = 0x00
    halted = False
    while not halted:
        opcode = memory[addr]
        instruction = OPCODES.get(opcode)
        print(f"addr: {addr:02X}, opcode: {opcode:02X}, instruction: {instruction}, acc: {acc:06X}")
        if instruction == "HLT":
            halted = True
        addr += 1

        if instruction == "NOP":
            pass
        elif instruction == "LDA":
            from_addr = lda24(memory, addr)
            acc = lda24(memory, from_addr)
        elif instruction == "ADD":
            from_addr = lda24(memory, addr)
            acc += lda24(memory, from_addr)
        elif instruction == "STA":
            write_addr = lda24(memory, addr)
            memory = sta24(memory, write_addr, acc)
        elif instruction == "INC":
            acc += 1
        elif instruction == "DEC":
            acc -= 1

        addr += 3

    return memory

if __name__ == "__main__":
    bin_file = sys.argv[1]

    with open(bin_file, "rb") as f:
        memory = pickle.load(f)

    print(f"Loading memory...")
    dump_memory(memory)
    print(f"\nRunning...")
    memory = run(memory)
    print(f"\nMemory after running...")
    dump_memory(memory)

