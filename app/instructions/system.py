from app.instructions import instruction

@instruction("NOP", 0x00)
def nop(cpu):
    """
    No operation.
    """
    return True

@instruction("HLT", 0xF0)
def hlt(cpu):
    """
    Halt the CPU.
    """
    cpu.halted = True
    return False

@instruction("DEBUG", 0xFF)
def debug(cpu):
    """
    Print the current state of the CPU.
    """
    # print(f" (DEBUG CMD) ==> PC: {cpu.PC:02X} A: {cpu.A:02X} X: {cpu.X:02X} Y: {cpu.Y:02X} SP: {cpu.SP:02X} Flags: {cpu.flags}")
    print("\n\n===========================D E B U G===========================                                                            ")
    cpu.stat(with_stack=True)
    return True

@instruction("CLFZ", 0xFE)
def clfz(cpu):
    """
    Clear the zero flag.
    """
    cpu.flags["Z"] = False
    return True


@instruction("CLFK", 0xFD)
def clfk(cpu):
    """
    Clear the keyboard flag.
    """
    cpu.memory.clear_kb_flag()
    return True

@instruction("DMPKB", 0xFC)
def dmpkb(cpu):
    """
    Dump the keyboard buffer to the video memory.
    """
    cpu.memory.dump_kb_buffer()
    return True
