from app.instructions import instruction

@instruction("CMP", 0x20)
def cmp(cpu):
    """
    Compare the value in the program counter with the accumulator.
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.flags["Z"] = cpu.A == value  # Set the zero flag if the values are equal
    return True

@instruction("CMPI", 0x21)
def cmpi(cpu):
    """
    Compare the value in the program counter with the accumulator. (Compare Immediate)
    """
    # print(f"PC: {hex(cpu.PC)}")
    # print(f"A: {hex(cpu.A)}")
    value = cpu.read_memory(cpu.PC)
    # print(f"Value: {hex(value)}")
    # print(f"Comparing {hex(cpu.A)} (type: {type(cpu.A)}) with {hex(value)} (type: {type(value)})")
    cpu.flags["Z"] = hex(cpu.A) == hex(value)  # Set the zero flag if the values are equal
    return True


@instruction("ADD", 0x22)
def add(cpu):
    """
    Add the value in the program counter to the accumulator.
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.A += value
    return True

@instruction("ADDI", 0x23)
def addi(cpu):
    """
    Add the value in the program counter to the accumulator. (Add Immediate)
    """
    value = cpu.read_memory(cpu.PC)
    cpu.A += value
    return True

@instruction("SUB", 0x24)
def sub(cpu):
    """
    Subtract the value in the program counter from the accumulator.
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.A -= value
    return True

@instruction("SUBI", 0x25)
def subi(cpu):
    """
    Subtract the value in the program counter from the accumulator. (Subtract Immediate)
    """
    value = cpu.read_memory(cpu.PC)
    cpu.A -= value

@instruction("MUL", 0x26)
def mul(cpu):
    """
    Multiply the value in the program counter with the accumulator.
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.A *= value
    return True

@instruction("MULI", 0x27)
def muli(cpu):
    """
    Multiply the value in the program counter with the accumulator. (Multiply Immediate)
    """
    value = cpu.read_memory(cpu.PC)
    cpu.A *= value
    return True

@instruction("DIV", 0x28)
def div(cpu):
    """
    Divide the value in the program counter by the accumulator. (Integer Division)
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.A //= value
    return True

@instruction("DIVI", 0x29)
def divi(cpu):
    """
    Divide the value in the program counter by the accumulator. (Integer Division Immediate)
    """
    value = cpu.read_memory(cpu.PC)
    cpu.A //= value
    return True

@instruction("MOD", 0x2A)
def mod(cpu):
    """
    Modulo the value in the program counter by the accumulator.
    """
    value_addr = cpu.read_memory(cpu.PC)
    value = cpu.read_memory(value_addr)
    cpu.A %= value
    return True

@instruction("MODI", 0x2B)
def modi(cpu):
    """
    Modulo the value in the program counter by the accumulator. (Modulo Immediate)
    """
    value = cpu.read_memory(cpu.PC)
    cpu.A %= value
    return True