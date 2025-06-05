import os
import importlib


instruction_set = {}
opcode_map = {}
mnemonic_map = {}


def instruction(mnemonic, opcode):
    def decorator(fn):
        if opcode in opcode_map:
            raise ValueError(f"Opcode {opcode} already exists")
        if mnemonic in mnemonic_map:
            raise ValueError(f"Mnemonic {mnemonic} already exists")

        instruction_set[mnemonic] = fn
        opcode_map[opcode] = mnemonic
        mnemonic_map[mnemonic] = (opcode)
        return fn
    return decorator
