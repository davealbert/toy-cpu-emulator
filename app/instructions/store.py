from app.instructions import instruction

@instruction("STA", 0x30)
def sta(cpu):
    """
    Store the accumulator in the program counter.
    """
    value_addr = cpu.read_memory(cpu.PC)
    cpu.write_memory(value_addr, cpu.A)
    return True

@instruction("STX", 0x31)
def stx(cpu):
    """
    Store the X register in the program counter.
    """
    value_addr = cpu.read_memory(cpu.PC)
    cpu.write_memory(value_addr, cpu.X)
    return True

@instruction("STY", 0x32)
def sty(cpu):
    """
    Store the Y register in the program counter.
    """
    value_addr = cpu.read_memory(cpu.PC)
    cpu.write_memory(value_addr, cpu.Y)
    return True

