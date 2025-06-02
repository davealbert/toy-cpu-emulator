LDA num1      ; Load initial number
ADD num2      ; Add value at label num2 to acc
ADD num3      ; Add value at label num3 to acc
ADD num4      ; Add value at label num4 to acc
STA result    ; Store Results

top:
DEC
JZ end
JMP top

end:
HLT           ; Halt execution


num1:
    0x02

num2:
    0x03

num3:
    0x04

num4:
    0x07

result:
