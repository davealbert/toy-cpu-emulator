MEMORY_SIZE = 16 * 6

def zero_memory_map(size):
    return {i: 0 for i in range(size)}

def dump_memory(memory):
    for addr in range(0, len(memory), 16):
        print(
            f"{addr:02X}| {memory[addr]:02X} {memory[addr + 1]:02X} {memory[addr + 2]:02X} {memory[addr + 3]:02X}"
            f"   {memory[addr + 4]:02X} {memory[addr + 5]:02X} {memory[addr + 6]:02X} {memory[addr + 7]:02X}"
            f"   {memory[addr + 8]:02X} {memory[addr + 9]:02X} {memory[addr + 10]:02X} {memory[addr + 11]:02X}"
            f"   {memory[addr + 12]:02X} {memory[addr + 13]:02X} {memory[addr + 14]:02X} {memory[addr + 15]:02X}"
        )
