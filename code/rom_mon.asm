MAIN:
    ;Wait for command loop
WAIT_FOR_INPUT:
    LDA 0xFF0800         ; Read keyboard input
    CMPI 0x00             ; Check if input is 0
    JZ WAIT_FOR_INPUT   ; If input is 0, wait for input again

    CALL READ_COMMAND
    CLFK
    JMP WAIT_FOR_INPUT

READ_COMMAND:
    ;CLFZ
    LDA 0xFF0804         ; Read keyboard input
    CMPI 0x71            ; Check if input is 'q'
    JZ PROCESS_QUIT      ; If input is 'q', process quit

    ; DEBUG
    CMPI 0x64            ; Check if input is 'd'
    JZ CALL_DEBUG

    ; WRITE_DISPLAY_MEMORY
    CMPI 0x77            ; Check if input is 'w'
    JZ WRITE_DISPLAY_MEMORY
    RET

PROCESS_QUIT:
    HLT

CALL_DEBUG:
    DEBUG
    RET

WRITE_DISPLAY_MEMORY:
    ;LDIY 0x58         ; value for X
    ;STY 0xFF0004         ; Write value to memory
    DMPKB
    RET
