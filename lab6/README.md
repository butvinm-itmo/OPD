#### «Национальный исследовательский университет ИТМО»
### Основы профессиональной деятельности
## Лабораторная работа 7
## Вариант 3050-
### Бутвин Михаил, P3130
###  2023

<div style="clear: both; page-break-after: always;"></div>

-------

## Task

MUL М - Знаковое умножение младших байтов аккумулятора и ячейки памяти, результат в AC, установить признаки N/Z/V/C
Код операции - 9...
Тестовая программа должна начинаться с адреса 044D16

## Source

| Adr | Code       | Label      | Description                            | Comment                                                                                                                                                                    |
| --- | ---------- | ---------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E0  | 80EF804002 |            | if CR(15) = 0 then GOTO RESERVED @ EF  | Check that command is 9XXX                                                                                                                                                 |
| E1  | 81EF404002 |            | if CR(14) = 1 then GOTO RESERVED @ EF  |
| E2  | 0020E00000 | MUL        | 0 ? BR, N, Z, V, C                     | Reset buffer                                                                                                                                                               |
| E3  | 0001C11001 | MUL_EXT    | extend sign DR(0..7) ? DR, N, Z, V     | Extend low bytes                                                                                                                                                           |
| E4  | 0010C11010 |            | extend sign AC(0..7) ? AC, N, Z, V     |
| E5  | 80E8089040 | MUL_INV    | if PS(N) = 0 then GOTO MUL_CHKADD @ E8 | AC will be used as counter, so it always should be positive. To achieve this, we negate both AC and DC if AC is negative.                                                  |
| E6  | 0010E09610 |            | NEG(AC) ? AC, N, Z, V, C               |
| E7  | 0001E09501 |            | NEG(DR) ? DR, N, Z, V, C               |
| E8  | 80EA019010 | MUL_CHKADD | if AC(0) = 0 then GOTO MUL_SHDR @ EA   | If AC ends with zero bit, we skip summation                                                                                                                                |
| E9  | 0020E09021 | MUL_ADD    | BR + DR ? BR, N, Z, V, C               | Sum DR to BR                                                                                                                                                               |
| EA  | 0001020001 | MUL_SHDR   | SHL(DR) ? DR                           | Shift DR to the left                                                                                                                                                       |
| EB  | 0010880010 | MUL_SHAC   | ASR(AC) ? AC, N, Z                     | Shift AC to the right                                                                                                                                                      |
| EC  | 80E8049040 | MUL_CHKAC0 | if PS(Z) = 0 then GOTO MUL_CHKADD @ E8 | If AC is not zero, we continue summation                                                                                                                                   |
| ED  | 0010809020 | MUL_FINISH | BR ? AC, N, Z                          | Otherwise, save result from buffer to AC and set flags. V and C is always 0 due to result of a multiplication of two 8-bit numbers is always less than 16-bit signed numbe |
| EE  | 80C4101040 |            | GOTO INT @ C4                          | Go to interrupt cycle                                                                                                                                                      |

## Testing

See code of tests generator in `test.py`

Test template:
```basm
ld #0x{a_hex} ; {a} * {b} = {r}
word 0x9f{b_hex}
test_flags{i}:
    test_n{i}: {"bnc" if n else "bns"} fail{i} ; n = {n}
    test_z{i}: {"bnc" if n else "bns"} fail{i} ; z = {z}
test_result{i}:
    cmp $r{i}
    bne fail{i}
    jump pass{i}
fail{i}:
    ld #0x1
    hlt
pass{i}:
```


## Trace

Program:
```basm
start:
    ld #0xf5 ; -11
    word 0x9011 ; 11
    ; 0xf5 * 0x0b = -0x0a
```

Trace:
| Adr | Micro Cmd  | IP  | CR   | AR  | DR   | SP  | BR   | AC   | NZVC | СчМК |
| --- | ---------- | --- | ---- | --- | ---- | --- | ---- | ---- | ---- | ---- |
| E0  | 80EF804002 | 012 | 9011 | 011 | 9011 | 000 | 0011 | FFF5 | 1000 | E1   |
| E1  | 81EF404002 | 012 | 9011 | 011 | 9011 | 000 | 0011 | FFF5 | 1000 | E2   |
| E2  | 0020E00000 | 012 | 9011 | 011 | 9011 | 000 | 0000 | FFF5 | 0100 | E3   |
| E3  | 0001C11001 | 012 | 9011 | 011 | 0011 | 000 | 0000 | FFF5 | 0000 | E4   |
| E4  | 0010C11010 | 012 | 9011 | 011 | 0011 | 000 | 0000 | FFF5 | 1000 | E5   |
| E5  | 80E8089040 | 012 | 9011 | 011 | 0011 | 000 | 0000 | FFF5 | 1000 | E6   |
| E6  | 0010E09610 | 012 | 9011 | 011 | 0011 | 000 | 0000 | 000B | 0000 | E7   |
| E7  | 0001E09501 | 012 | 9011 | 011 | FFEF | 000 | 0000 | 000B | 1000 | E8   |
| E8  | 80EA019010 | 012 | 9011 | 011 | FFEF | 000 | 0000 | 000B | 1000 | E9   |
| E9  | 0020E09021 | 012 | 9011 | 011 | FFEF | 000 | FFEF | 000B | 1000 | EA   |
| EA  | 0001020001 | 012 | 9011 | 011 | FFDE | 000 | FFEF | 000B | 1000 | EB   |
| EB  | 0010880010 | 012 | 9011 | 011 | FFDE | 000 | FFEF | 0005 | 0000 | EC   |
| EC  | 80E8049040 | 012 | 9011 | 011 | FFDE | 000 | FFEF | 0005 | 0000 | E8   |
| E8  | 80EA019010 | 012 | 9011 | 011 | FFDE | 000 | FFEF | 0005 | 0000 | E9   |
| E9  | 0020E09021 | 012 | 9011 | 011 | FFDE | 000 | FFCD | 0005 | 1001 | EA   |
| EA  | 0001020001 | 012 | 9011 | 011 | FFBC | 000 | FFCD | 0005 | 1001 | EB   |
| EB  | 0010880010 | 012 | 9011 | 011 | FFBC | 000 | FFCD | 0002 | 0001 | EC   |
| EC  | 80E8049040 | 012 | 9011 | 011 | FFBC | 000 | FFCD | 0002 | 0001 | E8   |
| E8  | 80EA019010 | 012 | 9011 | 011 | FFBC | 000 | FFCD | 0002 | 0001 | EA   |
| EA  | 0001020001 | 012 | 9011 | 011 | FF78 | 000 | FFCD | 0002 | 0001 | EB   |
| EB  | 0010880010 | 012 | 9011 | 011 | FF78 | 000 | FFCD | 0001 | 0001 | EC   |
| EC  | 80E8049040 | 012 | 9011 | 011 | FF78 | 000 | FFCD | 0001 | 0001 | E8   |
| E8  | 80EA019010 | 012 | 9011 | 011 | FF78 | 000 | FFCD | 0001 | 0001 | E9   |
| E9  | 0020E09021 | 012 | 9011 | 011 | FF78 | 000 | FF45 | 0001 | 1001 | EA   |
| EA  | 0001020001 | 012 | 9011 | 011 | FEF0 | 000 | FF45 | 0001 | 1001 | EB   |
| EB  | 0010880010 | 012 | 9011 | 011 | FEF0 | 000 | FF45 | 0000 | 0101 | EC   |
| EC  | 80E8049040 | 012 | 9011 | 011 | FEF0 | 000 | FF45 | 0000 | 0101 | ED   |
| ED  | 0010809020 | 012 | 9011 | 011 | FEF0 | 000 | FF45 | FF45 | 1001 | EE   |

## Testing guide

1. Generate tests with `test.py`
2. Run BComp with `java -jar -Dmode=dual bcomp.jar`
3. Load new commands
4. Load `test.basm`
5. Run program
6. Make a coffee or tea
7. Come back and check that `AC == 0` and `IP = 0x7f0`
8. Load `test_incorrect.basm`
9. Run program
10. Watch some short YouTube video while drinking coffee or tea
11. Come back and check that `AC == 0` and `IP = 0x7f0`
12. Load `test_manual.basm`
13. Run program step-by-step and check algorithm correctness
