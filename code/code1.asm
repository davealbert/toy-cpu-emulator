LDA num1      ; Load initial number
ADD num2      ; Add value at label num2 to acc
ADD num3      ; Add value at label num3 to acc
ADD num4      ; Add value at label num4 to acc
STA result    ; Store Results

CLZ
top:
DEC
CMP
JNZ top

end:
STA result2
HLT           ; Halt execution


num1:
    0x02

num2:
    0x02

num3:
    0x01

num4:
    0x01

result:
    0xFFFFFF

result2:
    0xFFFFFF

result3:
    0xFFFFFF
