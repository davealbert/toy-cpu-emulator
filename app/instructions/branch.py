from app.instructions import instruction

# │   ├── load.py        # LDA, LDX, LDY, etc.
# │   ├── store.py       # STA, STX, STY
# │   ├── math.py        # ADD, SUB, MUL, DIV, etc.
# │   ├── branch.py      # JMP, JZ, JNZ, etc.
# │   ├── stack.py       # PHA, PLA, etc.


# TODO: JMP, JZ, JNZ, etc.

@instruction("JMP", 0x01)
def jmp(cpu):
    """
    Jump to the address in the program counter.
    """
    cpu.PC = cpu.read_memory(cpu.PC)
    return False

@instruction("JZ", 0x02)
def jz(cpu):
    """
    Jump to the address in the program counter if the zero flag is set.
    """
    if cpu.flags["Z"]:
        cpu.PC = cpu.read_memory(cpu.PC)
        # print(f"JZ: PC = {cpu.PC:02X}")
        return False
    return True

@instruction("JNZ", 0x03)
def jnz(cpu):
    """
    Jump to the address in the program counter if the zero flag is not set.
    """
    if not cpu.flags["Z"]:
        cpu.PC = cpu.read_memory(cpu.PC)
        return False
    return True

@instruction("CALL", 0x04)
def call(cpu):
    """
    Call the address in the program counter.
    """
    cpu.stack_push(cpu.PC + cpu.word_size)
    cpu.PC = cpu.read_memory(cpu.PC)
    return False

@instruction("RET", 0x05)
def ret(cpu):
    """
    Return from the address in the program counter.
    """
    cpu.PC = cpu.stack_pop()
    return False
