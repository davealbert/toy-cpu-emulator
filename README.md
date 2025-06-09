# My CPU Emulator

A fun learning project implementing a simple CPU emulator in Python. This project simulates a basic computer system with a custom instruction set, memory management, and I/O capabilities.

## Overview

This project implements a simple CPU architecture with the following features:

- 24-bit word size
- Basic register set (A, X, Y, SP)
- Status flags (Zero flag)
- Memory-mapped I/O for keyboard input and display
- Stack operations
- Simple instruction set including:
  - Load/Store operations
  - Arithmetic operations (ADD, SUB, MUL, DIV)
  - Comparison and branching
  - System operations (NOP, HLT, DEBUG)
  - Stack operations (PUSH/POP)

## Project Structure

- `app/` - Main application code
  - `cpu.py` - CPU implementation
  - `memory.py` - Memory management
  - `instructions/` - Instruction set implementation
    - Various instruction modules (math.py, load.py, system.py, etc.)
- `code/` - Assembly code examples
- `disk/` - Storage for program binaries
- `.vscode/` - VS Code configuration

## Instruction Set

The CPU supports various instructions including:

- Data Movement: `LDA`, `LDX`, `LDY`, `STA`, `STX`, `STY`
- Arithmetic: `ADD`, `SUB`, `MUL`, `DIV` (with immediate variants)
- Comparison: `CMP`, `CMPI`
- Control Flow: `JMP`, `JZ`, `JNZ`, `CALL`
- Stack Operations: `PHA`, `PHX`, `PHY`, `PLA`, `PLX`, `PLY`
- System: `NOP`, `HLT`, `DEBUG`

## Running the Emulator

To run the emulator:

```bash
python -m app.run <binary_file>
```


How I've been running it for testing and debugging:
```bash
python -m app.asm code/rom_mon.asm app/roms/rom_mon.bin && DEBUG=1 CLOCK_SPEED=1000 python -m app.run app/roms/rom_mon.bin
```


Environment variables:
- `DEBUG=1` - Enable debug mode
- `CLOCK_SPEED=<number>` - Set CPU clock speed (ticks per second, default: 3)

## Learning Purpose

This project was created for learning and fun, to understand:
- How CPUs work at a basic level
- Instruction set architecture (ISA) design
- Memory management and I/O
- Assembly language programming
- Emulator implementation

Feel free to explore, modify, and learn from this project! It's a great way to understand computer architecture fundamentals in a hands-on way.
