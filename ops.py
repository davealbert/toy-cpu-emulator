OPCODES = {
    0x00: "NOP",

    0x10: "LDA",

    0x20: "ADD",

    0x30: "STA",

    0x40: "LDI",

    0x50: "STI",

    0x60: "JMP",
    0x61: "JNZ",
    0x62: "JZ",
    # 0x63: "JEQ",
    # 0x64: "JNE",
    # 0x65: "JGT",
    # 0x66: "JLT",
    # 0x67: "JGE",
    # 0x68: "JLE",

    0x70: "INC",
    0x71: "DEC",

    # 0x80: "AND",
    # 0x81: "OR",
    # 0x82: "XOR",
    # 0x83: "NOT",


    0x91: "SHR",



    0xF0: "HLT",
}

MNEMONICS = {v: k for k, v in OPCODES.items()}

def sta24(mem, addr, acc):
    mem[addr]     = acc & 0xFF
    mem[addr + 1] = (acc >> 8) & 0xFF
    mem[addr + 2] = (acc >> 16) & 0xFF
    return mem

def lda24(mem, addr):
    return mem[addr] | (mem[addr + 1] << 8) | (mem[addr + 2] << 16)

