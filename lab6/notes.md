9XXX = 1001 X X X

| bit range | 39              | 35        | 31   | 27   | 23             | 19   | 15   | 11   | 7    | 3         |
| --------- | --------------- | --------- | ---- | ---- | -------------- | ---- | ---- | ---- | ---- | --------- |
| value     | 1000            | 0001      | 1010 | 0010 | 1000           | 0000 | 0001 | 0000 | 0000 | 0010      |
| descr     | Control command | if 1      | GOTO A2     | 7th bit of commutator | LTOL |      |      | CR -> ALU |



| Bit range | 39              | 35        | 31   | 27   | 23              | 19   | 15   | 11   | 7    | 3         |
| --------- | --------------- | --------- | ---- | ---- | --------------- | ---- | ---- | ---- | ---- | --------- |
| Value     | 1000            | 0001      | 0000 | 1001 | 1000            | 0000 | 0100 | 0000 | 0000 | 0010      |
| Descr     | Control command | if 1      | GOTO 09     | 15th bit of commutator | HTOL |      |      | CR -> ALU |


| Bit range | 39              | 35        | 31   | 27   | 23              | 19   | 15   | 11   | 7    | 3         |
| --------- | --------------- | --------- | ---- | ---- | --------------- | ---- | ---- | ---- | ---- | --------- |
| Value     | 1000            | 0001      | 1110 | 0000 | 1000            | 0000 | 0100 | 0000 | 0000 | 0010      |
| Descr     | Control command | if 1      | GOTO E0     | 15th bit of commutator | HTOL |      |      | CR -> ALU |



E0 81FF404002   RESERVED        If CR(14) = 1 then GOTO UNRESOLVED @ FF
E1 81FF204002                   If CR(13) = 1 then GOTO UNRESOLVED @ FF
E2 80FF104002                   If CR(12) = 0 then GOTO UNRESOLVED @ FF


>>> def b(h):
...     return ' '.join(bin(int(hi, 16))[2:].zfill(4) for hi in h)


```basm
start:
; 30 * -46 = -1380
ld #0x1e
word 0x9fd2
cmp $r0
beq ok0
hlt
```

