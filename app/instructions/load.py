from app.instructions import instruction


@instruction("LDA", 0x10)
def lda(cpu):
    """
    Load the accumulator with the value at the address in the program counter.
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.A = value
    return True

@instruction("LDIA", 0x11)
def ldia(cpu):
    """
    Load the accumulator with the value in the program counter. (Load Immediate)
    """
    value = cpu.read_memory(cpu.PC)
    cpu.A = value
    return True

@instruction("LDX", 0x12)
def ldx(cpu):
    """
    Load the X register with the value at the address in the program counter.
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.X = value
    return True

@instruction("LDIX", 0x13)
def ldix(cpu):
    """
    Load the X register with the value in the program counter. (Load Immediate)
    """
    value = cpu.read_memory(cpu.PC)
    cpu.X = value
    return True

@instruction("LDY", 0x14)
def ldy(cpu):
    """
    Load the Y register with the value at the address in the program counter.
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.Y = value
    return True

@instruction("LDIY", 0x15)
def ldiy(cpu):
    """
    Load the Y register with the value in the program counter. (Load Immediate)
    """
    value = cpu.read_memory(cpu.PC)
    cpu.Y = value
    return True




