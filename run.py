import sys
from memory import MemoryManager
from ops import OPCODES
from time import sleep

CLOCK_SPEED = 3  # 3 Ticks per second
# CLOCK_SPEED = 10  # 10 Ticks per second

def immediate_or_address(memory, program_counter):
    if memory.startswith("#"):
        # Immediate value
        value = int(memory[1:], 16)
    else:
        # Address
        from_addr = lda24(memory, program_counter)
        value = lda24(memory, from_addr)
    return value


def value_from_address(memory, program_counter):
    from_addr = memory.get_memory(program_counter)
    value = memory.get_memory_le24(from_addr)
    return value


def run(memory: MemoryManager, debug=False):
    def print_registers():
        print(
                f"program_counter: {program_counter:02X}, opcode: {opcode:02X}, instruction: {instruction}, "
                f"A: {registers['A']:06X}, X: {registers['X']:06X}, Y: {registers['Y']:06X}, "
                f"SP: {registers['SP']:06X}, "
                f"Z: {flags['Z']}"  #, N: {flags['N']}, C: {flags['C']}, V: {flags['V']}"
            )

    program_counter = 0x00
    halted = False
    registers = {
        "A": 0x00,   # Accumulator
        "X": 0x00,   # Index Register X
        "Y": 0x00,   # Index Register Y
        "SP": 0x00,  # Stack Pointer
    }
    flags = {
        "Z": False,  # Zero Flag
        # "N": False,  # Negative Flag
        # "C": False,  # Carry Flag
        # "V": False,  # Overflow Flag
    }

    stack = []

    print(f"{program_counter:02X}", end="")
    while not halted:
        sleep(1 / CLOCK_SPEED)
        print(f"\b\b.{program_counter:02X}", end="")

        opcode = memory.get_memory(program_counter)
        instruction = OPCODES.get(opcode)
        if debug:
            print_registers()

        if instruction == "HLT":
            halted = True
        program_counter += 1

        match instruction:

            case "DEBUG":
                print("\n-------------D E B U G-------------")
                memory.dump_memory(full=True)
                print_registers()
                print(f"Stack: {stack}")
                print(f"Program counter: {program_counter:02X}")
                print(f"Halted: {halted}\n===========================\n")

            # No operation
            case "NOP":
                pass

            # Load
            case "LDA":
                registers["A"] = value_from_address(memory, program_counter)
            case "LDX":
                registers["X"] = value_from_address(memory, program_counter)
            case "LDY":
                registers["Y"] = value_from_address(memory, program_counter)

            # Load immediate
            case "LDIA":
                value = memory.get_memory_le24(program_counter)
                registers["A"] = value
            case "LDIX":
                value = memory.get_memory_le24(program_counter)
                registers["X"] = value
            case "LDIY":
                value = memory.get_memory_le24(program_counter)
                registers["Y"] = value

            # Compare
            case "CMP":
                value = value_from_address(memory, program_counter)
                flags["Z"] = registers["A"] == value
            case "CMPI":
                value = memory.get_memory_le24(program_counter)
                flags["Z"] = registers["A"] == value

            # Arithmetic on register A
            case "ADD":
                registers["A"] += value_from_address(memory, program_counter)
            case "SUB":
                registers["A"] -= value_from_address(memory, program_counter)
            case "MUL":
                registers["A"] *= value_from_address(memory, program_counter)
            case "DIV":
                registers["A"] //= value_from_address(memory, program_counter)
            case "MOD":
                registers["A"] %= value_from_address(memory, program_counter)

            # Arithmetic on register A with immediate value
            case "ADDI":
                value = memory.get_memory_le24(program_counter)
                registers["A"] += value
            case "SUBI":
                value = memory.get_memory_le24(program_counter)
                registers["A"] -= value
            case "MULI":
                value = memory.get_memory_le24(program_counter)
                registers["A"] *= value
            case "DIVI":
                value = memory.get_memory_le24(program_counter)
                registers["A"] //= value
            case "MODI":
                value = memory.get_memory_le24(program_counter)
                registers["A"] %= value

            # Store
            case "STA":
                write_addr = memory.get_memory(program_counter)
                memory.set_memory_le24(write_addr, registers["A"])
            case "STX":
                write_addr = memory.get_memory(program_counter)
                memory.set_memory_le24(write_addr, registers["X"])
            case "STY":
                write_addr = memory.get_memory(program_counter)
                memory.set_memory_le24(write_addr, registers["Y"])

            # Stack PUSH
            case "PHA":
                # Push a copy of the accumulator onto the stack
                stack.append(registers["A"])
                registers["SP"] += 1
            case "PHX":
                stack.append(registers["X"])
                registers["SP"] += 1
            case "PHY":
                stack.append(registers["Y"])
                registers["SP"] += 1
            case "PUSI":
                value = memory.get_memory_le24(program_counter)
                stack.append(value)
                registers["SP"] += 1

            # Stack PULL/POP
            case "PLA":
                registers["A"] = stack.pop()
                registers["SP"] -= 1
            case "PLX":
                registers["X"] = stack.pop()
                registers["SP"] -= 1
            case "PLY":
                registers["Y"] = stack.pop()
                registers["SP"] -= 1

            # Flags
            case "CLFZ":
                flags["Z"] = False

            # Always jump
            case "JMP":
                program_counter = memory.get_memory_le24(program_counter)
                continue

            # Jump if not zero
            case "JNZ":
                if not flags["Z"]:
                    to_addr = memory.get_memory_le24(program_counter)
                    if debug:
                        print(f"            JNZ {to_addr:06X}")
                    program_counter = to_addr
                    continue
                # Zero, don't jump
                pass

            # Jump if zero
            case "JZ":
                if flags["Z"]:
                    to_addr = memory.get_memory_le24(program_counter)
                    if debug:
                        print(f"            JNZ {to_addr:06X}")
                    program_counter = to_addr
                    continue
                # Not zero, don't jump
                pass

            # Increment/Decrement
            case "INC":
                registers["A"] += 1
            case "INX":
                registers["X"] += 1
            case "INY":
                registers["Y"] += 1
            case "DEC":
                registers["A"] -= 1
            case "DEX":
                registers["X"] -= 1
            case "DEY":
                registers["Y"] -= 1

        # Add the data size to the program counter
        program_counter += 3

    # End of program
    print(f"\nHalted at program_counter: {program_counter:02X}")
    print_registers()


if __name__ == "__main__":
    bin_file = sys.argv[1]
    memory = MemoryManager(filename=bin_file)

    print(f"Loading memory...")
    memory.dump_memory(full=True)
    print(f"\nRunning...")
    run(memory, debug=False)
    # print(f"\nMemory after running...")
    # memory.dump_memory(full=True)

