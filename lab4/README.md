#### «Национальный исследовательский университет ИТМО»
### Основы профессиональной деятельности
## Лабораторная работа 5
## Вариант 3003
### Бутвин Михаил, P3130
###  2023

<div style="clear: both; page-break-after: always;"></div>

-------
## Constrains

-128 &le; 3x - 7 &ge; 127
-121 &le; 3x &ge; 134
-40 &le; 3x &ge; 44

## Source code

Use [Basm for VSCode](https://github.com/ohtie/bcomp-asm) to view with syntax highlighting.

```basm
org 0x000
int_dev_2_vec: word $int_dev_2, 0x100
int_dev_3_vec: word $int_dev_3, 0x180

org 0x033
x: word ?

; devices registers
; dev_2 DR = 4
; dev_2 MR, SR = 5
; dev_3 DR = 6
; dev_3 MR, SR = 7

org 0x100
f: ; (x: int) -> int
    ld &1 ; load x
    add &1 ; x * 3
    add &1
    st &1 ; store x
    ret

org 0x150
x_min: word 0xFFD8 ; -40
x_max: word 0x002C ; 44

constrain_x:
    ; -40 <= x <= 44 -> 0xFFD8 <= x <= 0x002C
    ld $x
    cmp x_min ; if x < 0xFFD8 then return
    blt constrain_x_set_min
    cmp x_max ; if x <= 0x002C then return
    blt constrain_x_ret
    beq constrain_x_ret
    ; else x = 0xFFD8
    constrain_x_set_min:
    ld x_min
    st $x
    constrain_x_ret:
    ret

org 0x200
int_dev_3:
    di
    ; show result of F(x) on dev_3
    nop ; debug
    ld $x
    push
    call $f
    pop
    out 6 ; dev_3 DR
    nop ; debug
    ei
    iret

org 0x300
int_dev_2:
    di
    ; x = (dev_2 DR) * 3 - x
    nop ; debug
    in 4 ; dev_2 DR
    push
    add &0 ; dev_dr * 3
    add &0
    sub $x ; x = dev_dr * 3 - x
    st $x
    call $constrain_x
    pop ; remove dev_dr
    nop ; debug
    ei
    iret

org 0x400
main:
    ; inc x by 3
    l1:
        ld $x
        add #0x3
        st $x
        call $constrain_x
    jump l1

start:
    di
    ld #0x8 ; (1000 | 0000) - enable interrupt and set vector int_dev_3_vec
    out 5 ; dev_2 MR
    ld #0x9 ; (1000 | 0001) - enable interrupt and set vector int_dev_3_vec
    out 7 ; dev_3 MR
    ei
    jump main

```

## Debug Guide
FFE1
FFA3

Проверка обработки прерываний:
2. Заменить NOP по нужному адресу на HLT.
1. Загрузить текст программы в БЭВМ.
3. Запустить программу в режиме РАБОТА.
4. Установить «Готовность ВУ-3».
5. Жди, пока программа не остановится.
6. Записать текущее значение X из памяти БЭВМ:
7. Нажми «Продолжение».
8. Запиши результат обработки прерывания - число F(x), которое появится в DR контроллера ВУ-3.
9.  Нажми «Продолжение».
10. Введи любое число на ВУ-2 и запиши его.
11. Подготовься к прерыванию на ВУ-2, нажав кнопку "Готовность ВУ-2".
12. Жди, пока программа не остановится.
13. Запиши число X
14. Нажми «Продолжение».
15. Запиши полученное значение X и сравни со значением (записанное число*3-записанный X)
16. Нажми «Продолжение».


Проверка основной программы:
1. Загрузи программу в БЭВМ.
2. Запиши в переменную X максимально возможное значение (0x002C).
3. Запусти программу в режиме останова.
4. Пройди нужное количество шагов программы и убедись, что когда X становится больше 0x002C, то его значение сбрасывается до минимального значения, которое допустимо по ОДЗ.
5. Аналогично проверь, что при уменьшении X до значения меньше 0xFFD8, его значение сбрасывается до минимального значения, которое допустимо по ОДЗ.

(0x2) * 3 - (0xffdb) = 0x6 + 0x25 = 0x2b

(0x4) * 3 - 0xffe7 = 0xc + 0x19 = 0x25

(0x4) * 3 - (0xffdb) = 0xC + 0x25 = 0x31

(0x4) * 3 - (0xffd8) = 0xC + 0x28 = 34

