import threading
import msvcrt
from app.memory import MemoryManager
from app.instructions import instruction_set, opcode_map
import os
import importlib
from time import sleep

# TODO: Load ROM from file ../roms/rom_mon.bin
# rom_path = os.path.join(os.path.dirname(__file__), "../roms", "rom_mon.bin")

DEFAULT_CLOCK_SPEED = 3  # 3 Ticks per second
# DEFAULT_CLOCK_SPEED = 10  # 10 Ticks per second

CLOCK_SPEED = int(os.getenv("CLOCK_SPEED", DEFAULT_CLOCK_SPEED))

def keyboard_thread(mem):
    while True:
        # TODO: This is only for Windows, need to implement a cross-platform solution later
        if msvcrt.kbhit():
            kb_char = msvcrt.getch().decode('utf-8', errors='ignore')
            mem.set_kb_flag()
            # print(f"     Keyboard input: {kb_char}  {type(kb_char)}")
            # print(f"     Keyboard input: {ord(kb_char)}  {type(ord(kb_char))}")
            # print(f"     Keyboard input: {hex(ord(kb_char))}  {type(hex(ord(kb_char)))}")
            mem.set_kb_char(ord(kb_char))

class CPU:
    def load_all_instructions(self, debug=False):
        if debug:
            print("    Loading instructions...")
        instructions_path = os.path.join(os.path.dirname(__file__), "instructions")
        for filename in os.listdir(instructions_path):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = f"app.instructions.{filename[:-3]}"
                if debug:
                    print(f"    Loading instruction: {filename[:-3]} ({module_name})")
                importlib.import_module(module_name)
        if debug:
            sorted_opcode_map = sorted(opcode_map.items(), key=lambda x: x[0])
            instruction_list = [f"0x{opcode:02X}\t{mnemonic}" for opcode, mnemonic in sorted_opcode_map]
            for instruction in instruction_list:
                print(instruction)
            print("    Instructions loaded.\n")


    def __init__(self, memory: MemoryManager, debug=False):
        self.memory = memory
        self.PC = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.SP = 0xFF  # To be implemented
        self.stack = []  # TODO: Implement stack in memory instead of a list
        self.flags = {
            "Z": False,
        }
        self.halted = False
        self._skip_pc_increment = False
        self.debug = debug
        self.load_all_instructions(debug=debug)
        self.operand_size = 3

        # Start the keyboard monitor thread
        self.keyboard_thread = threading.Thread(target=keyboard_thread, args=(self.memory,))
        self.keyboard_thread.daemon = True
        self.keyboard_thread.start()


    def skip_pc_increment(self):
        self._skip_pc_increment = True

    def move_pc(self, value):
        if self._skip_pc_increment:
            self._skip_pc_increment = False
            return
        self.PC += value

    def read_memory(self, address):
        return self.memory.get_memory_le24(address)

    def write_memory(self, address, value):
        self.memory.set_memory_le24(address, value)

    def clear_kb_flag(self):
        self.memory.clear_kb_flag()

    def tick(self):
        if not self.debug:
            print(".", end="", flush=True)

        opcode = self.memory.get_memory(self.PC)
        mnemonic = opcode_map.get(opcode)
        if mnemonic is None:
            print(
                f"PC: {self.PC:02X} A: {self.A:02X} X: {self.X:02X} "
                f"Y: {self.Y:02X} SP: {self.SP:02X} Flags: {self.flags} "
                f"{mnemonic} {opcode:02X} KB Flag: {self.memory.get_kb_flag()}, KB Char: {self.memory.get_kb_char()}"
            )
            raise ValueError(f"Unknown opcode: {opcode:02X}")
        instruction = instruction_set.get(mnemonic)
        self.move_pc(1)
        if self.debug:
            print(
                f"    PC: {self.PC:02X} A: {self.A:02X} X: {self.X:02X} "
                f"Y: {self.Y:02X} SP: {self.SP:02X} Flags: {self.flags} "
                f"{mnemonic} {opcode:02X} KB Flag: {self.memory.get_kb_flag()}, KB Char: {self.memory.get_kb_char()}"
            )
        should_step = instruction(self)
        if should_step:
            self.move_pc(3)

    def run(self, start_addr=0x00):
        if self.debug:
            print("  Running in debug mode.")
        self.PC = start_addr

        while not self.halted:
            self.tick()
            if self.memory.get_kb_flag():
                print("-", end="", flush=True)
            #     print(f"Keyboard input: {self.memory.get_kb_char()}")
            #     self.memory.clear_kb_flag()  # Don't clear the flag here, it will be cleared by the instruction
            sleep(1 / CLOCK_SPEED)

    def stat(self, with_stack=False):
        """Print out the current state of the CPU"""
        print(f"PC: {self.PC:02X} A: {self.A:02X} X: {self.X:02X} Y: {self.Y:02X} SP: {self.SP:02X} Flags: {self.flags}")
        print(f"   KB Flag: {self.memory.get_kb_flag()}, KB Char: {self.memory.get_kb_char()}")
        if with_stack:
            print(f"Stack: {self.stack}")

    def stack_push(self, value):
        # TODO: Implement stack in memory instead of a list
        self.SP -= 1
        self.stack.append(value)

    def stack_pop(self):
        # TODO: Implement stack in memory instead of a list
        self.SP += 1
        return self.stack.pop()

