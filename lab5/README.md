#### «Национальный исследовательский университет ИТМО»
### Основы профессиональной деятельности
## Лабораторная работа 6
## Вариант 3003
### Бутвин Михаил, P3130
###  2023

<div style="clear: both; page-break-after: always;"></div>

-------

# Source code

Use [Basm for VSCode](https://github.com/ohtie/bcomp-asm) to view with syntax highlighting.

```basm
ORG 0x5E7
RESULT: WORD ?

ORG 0x485
RESULT_POINTER: WORD $RESULT

START:
MAIN_LOOP:
    ; wait device ready
    WAIT_C1:
        IN 7
        AND #0x40
        BEQ WAIT_C1

    ; read c1 from device
    IN 6
    ; check NL
    CMP #0x0A
    BEQ STOP_AND_STORE_C1
    JUMP STORE_C1
    STOP_AND_STORE_C1:
        SWAB
        ST (RESULT_POINTER)
        HLT
    STORE_C1:
        ST (RESULT_POINTER)

    ; wait device ready
    WAIT_C2:
        IN 7
        AND #0x40
        BEQ WAIT_C2

    ; read c2 from device
    IN 6
    ; check NL
    CMP #0x0A
    BEQ STOP_AND_STORE_C2
    JUMP STORE_C2
    STOP_AND_STORE_C2:
        SWAB
        ADD (RESULT_POINTER)
        ST (RESULT_POINTER)+
        HLT
    STORE_C2:
        SWAB
        ADD (RESULT_POINTER)
        ST (RESULT_POINTER)+

    JUMP MAIN_LOOP
```

