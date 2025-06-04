OPCODES = {
    0x00: "NOP",

    # Load in to the register A, X or Y
    # With I the value is immediate as opposed to an address
    0x10: "LDA",
    0x11: "LDIA",
    0x12: "LDX",
    0x13: "LDIX",
    0x14: "LDY",
    0x15: "LDIY",


    # Arithmetic on register A
    # With I the value is immediate as opposed to an address
    0x20: "CMP",
    0x21: "CMPI",
    0x22: "ADD",
    0x23: "ADDI",
    0x24: "SUB",
    0x25: "SUBI",
    0x26: "MUL",
    0x27: "MULI",
    0x28: "DIV",    # Note this is integer division
    0x29: "DIVI",   # Note this is integer division
    0x2A: "MOD",
    0x2B: "MODI",


    # Store from the register A, X or Y to an address
    0x30: "STA",
    0x31: "STX",
    0x32: "STY",


    # Stack
    # Push
    0x40: "PHA",
    0x41: "PHX",
    0x42: "PHY",
    0x43: "PUSI",  # Push immediate

    # Pull / Pop
    0x44: "PLA",
    0x45: "PLX",
    0x46: "PLY",


    # Flags
    0x50: "CLFZ",


    # Jumps
    0x60: "JMP",
    0x61: "JNZ",
    0x62: "JZ",
    # 0x63: "CALL",
    # 0x64: "RET",


    # Increment
    0x70: "INC",
    0x71: "INX",
    0x72: "INY",


    # Decrement
    0x80: "DEC",
    0x81: "DEX",
    0x82: "DEY",


    # Halt
    0xF0: "HLT",


    # Debug
    0xFF: "DEBUG",
}

MNEMONICS = {v: k for k, v in OPCODES.items()}

# def sta24(mem, addr, acc):
#     mem[addr]     = acc & 0xFF
#     mem[addr + 1] = (acc >> 8) & 0xFF
#     mem[addr + 2] = (acc >> 16) & 0xFF
#     return mem

# def lda24(mem, addr):
#     return mem[addr] | (mem[addr + 1] << 8) | (mem[addr + 2] << 16)

