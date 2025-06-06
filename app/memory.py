import pickle

MEMORY_SIZE = 2 ** 24  # 16MB

class MemoryManager:
    stack_low = 0x00FF00
    stack_high = 0x00FFFF

    video_low = 0xFF0000
    # video_high = 0xFF07FF
    video_high = 0xFF0010

    kb_flag = 0xFF0800
    kb_char_low = 0xFF0804  # This must be at the start of a word boundary
    kb_char_high = 0xFF08FF

    rom_low = 0xFFF000
    rom_high = 0xFFFFFF

    def __init__(self, size=MEMORY_SIZE, filename=None):
        if filename:
            with open(filename, "rb") as f:
                self.memory = pickle.load(f)
        else:
            self.memory = {}

    def set_memory(self, addr, value):
        if addr >= self.stack_low and addr <= self.stack_high:
            print(f"Trying to update stack at {addr:06X} with {value:02X}")
            raise ValueError("Invalid memory address (reserved for stack)")
        if addr >= self.kb_flag and addr <= self.kb_char_high:
            print(f"Trying to update keyboard at {addr:06X} with {value:02X}")
            raise ValueError("Invalid memory address (reserved for keyboard)")
        if addr >= self.rom_low and addr <= self.rom_high:
            print(f"Trying to update ROM at {addr:06X} with {value:02X}")
            raise ValueError("Invalid memory address (reserved for ROM)")
        self.memory[addr] = value
        # if addr >= self.video_low and addr <= self.video_high:
        #     print(f"Should update video display at {addr:06X} with {value:02X}")

    def set_memory_le24(self, addr, value):
        self.set_memory(addr,     value & 0xFF)
        self.set_memory(addr + 1, (value >> 8) & 0xFF)
        self.set_memory(addr + 2, (value >> 16) & 0xFF)

    def get_memory_le24(self, addr):
        return self.get_memory(addr) | (self.get_memory(addr + 1) << 8) | (self.get_memory(addr + 2) << 16)

    def get_memory(self, addr):
        if addr >= self.stack_low and addr <= self.stack_high:
            raise ValueError("Invalid memory address (reserved for stack)")
        return self.memory.get(addr, 0)

    # Keyboard
    def set_kb_flag(self):
        self.memory[self.kb_flag] = 0x01

    def clear_kb_flag(self):
        self.memory[self.kb_flag] = 0x00

    def get_kb_flag(self):
        return self.memory.get(self.kb_flag, 0)

    def set_kb_char(self, value):
        self.memory[self.kb_char_low] = value & 0xFF

    def get_kb_char(self):
        # TODO: update kb to handle more than 1 character later
        return self.memory.get(self.kb_char_low, 0)

    # ROM
    def set_rom(self, addr, value):
        self.memory[addr] = value

    def get_rom(self, addr):
        return self.memory.get(addr, 0)

    def get_rom_range(self, start, end):
        return {addr: self.get_rom(addr) for addr in range(start, end)}

    def dump_memory(self, start=0x0000, end=0x0100, full=False):
        if full:
            start = 0x0000
            # Get the last address
            end = max(self.memory.keys())
        for addr in range(start, end, 16):
            row = [self.memory.get(addr + i, 0) for i in range(16)]
            quads = [' '.join(f"{row[i + j]:02X}" for j in range(4)) for i in range(0, 16, 4)]
            print(f"{addr:06X} | {'   '.join(quads)}")
