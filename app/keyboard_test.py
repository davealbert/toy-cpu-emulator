import threading
import sys
import time
import msvcrt

kb_flag = threading.Event()
kb_char = None

def keyboard_thread():
    global kb_char
    while True:
        if msvcrt.kbhit():
            kb_char = msvcrt.getch().decode('utf-8', errors='ignore')
            kb_flag.set()

thread = threading.Thread(target=keyboard_thread)
thread.daemon = True  # Set as daemon thread to ensure it exits with the main program
thread.start()

try:
    while True:
        if kb_flag.is_set():
            print(f"\n\nKeyboard input: {kb_char}")
            if kb_char.lower() == 'q':
                break
        kb_flag.clear()
        print(".", end="", flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting...")
    pass
