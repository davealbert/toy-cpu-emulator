from app.instructions import instruction

@instruction("PHA", 0x40)
def pha(cpu):
    """
    Push the accumulator to the stack.
    """
    cpu.stack_push(cpu.A)
    return True

@instruction("PLA", 0x41)
def pla(cpu):
    """
    Pop the accumulator from the stack.
    """
    cpu.A = cpu.stack_pop()
    return True

@instruction("PHX", 0x42)
def phx(cpu):
    """
    Push the X register to the stack.
    """
    cpu.stack_push(cpu.X)
    return True

@instruction("PLX", 0x43)
def plx(cpu):
    """
    Pop the X register from the stack.
    """
    cpu.X = cpu.stack_pop()
    return True

@instruction("PHY", 0x44)
def phy(cpu):
    """
    Push the Y register to the stack.
    """
    cpu.stack_push(cpu.Y)
    return True

@instruction("PLY", 0x45)
def ply(cpu):
    """
    Pop the Y register from the stack.
    """
    cpu.Y = cpu.stack_pop()
    return True

@instruction("PHSP", 0x46)
def phsp(cpu):
    """
    Push the stack pointer to the stack.
    """
    cpu.stack_push(cpu.SP)
    return True

@instruction("PLSP", 0x47)
def plsp(cpu):
    """
    Pop the stack pointer from the stack.
    """
    cpu.SP = cpu.stack_pop()
    return True

@instruction("PHI", 0x48)
def phi(cpu):
    """
    Push the value at the address in the program counter to the stack. (Push Immediate)
    """
    cpu.stack_push(cpu.read_memory(cpu.PC))
    return True

@instruction("PLI", 0x49)
def pli(cpu):
    """
    Pop the value from the stack to the address in the program counter. (Pop Immediate)
    """
    value_addr = cpu.read_memory(cpu.PC)
    cpu.write_memory(value_addr, cpu.stack_pop())
    return True
