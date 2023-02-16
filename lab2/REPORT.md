#### «Национальный исследовательский университет ИТМО»
### Основы профессиональной деятельности
## Лабораторная работа 3
## Вариант 3001
### Бутвин Михаил, P3130
###  2023

<div style="clear: both; page-break-after: always;"></div>

-------

## Source

| Адрес | Значение | Мнемоника    | Комментарий                                                                                                                                                                           |
| ----- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 253   | 0268     |              | **`array_st_pointer`**                                                                                                                                                                |
| 254   | A000     |              | **`array_curr_pointer`**                                                                                                                                                              |
| 255   | E000     |              | **`loop_counter`**                                                                                                                                                                    |
| 256   | 0200     |              | **`result`**                                                                                                                                                                          |
| 257 + | 0200     | CLA          | Begin of program. Clear accumulator                                                                                                                                                   |
| 258   | EEFD     | ST (IP-3)    | Store accumulator value to **`result`** cell                                                                                                                                          |
| 259   | AF04     | LD #4        | Load 4 to accumulator                                                                                                                                                                 |
| 25A   | EEFA     | ST (IP-6)    | Store accumulator value to **`loop_counter`** cell                                                                                                                                    |
| 25B   | AEF7     | LD (IP-9)    | Load value of **`array_st_pointer`** to accumulator                                                                                                                                   |
| 25C   | EEF7     | ST (IP-9)    | Store accumulator value to **`array_curr_pointer`** cell                                                                                                                              |
| 25D   | AAF6     | LD (IP-10)+  | Loop body beginning. Uses value of **`array_curr_pointer`** as operand address, so value from array at this address will be loaded to accumulator. Increment **`array_curr_pointer`** |
| 25E   | 0480     | ROR          | Shift accumulator and carry flag right                                                                                                                                                |
| 25F   | F401     | BCS (IP+1)   | Continue execution from (0x260 + 1) if carry flag (accumulator last bit due to ROR) is 1 else go to end of loop                                                                       |
| 260   | CE04     | JUMP (IP+4)  | Go to end of loop (0x261 + 4)                                                                                                                                                         |
| 261   | 0400     | ROL          | Shift accumulator and carry flag left (restore value)                                                                                                                                 |
| 262   | AEF3     | LD (IP-13)   | Load value of **`result`** to accumulator                                                                                                                                             |
| 263   | 0700     | INC          | Increment accumulator                                                                                                                                                                 |
| 264   | EEF1     | ST (IP-15)   | Store accumulator value to **`result`** cell                                                                                                                                          |
| 265   | 8255     | LOOP 0x255   | If **`loop_counter`** is 0 exit program (go to 0x266) else go to loop body beginning                                                                                                  |
| 266   | CEF6     | JUMP (IP-10) | Go to loop body beginning (0x267 - 10 = 0x25D)                                                                                                                                        |
| 267   | 0100     | HLT          | Exit program                                                                                                                                                                          |
| 268   | 0280     |              | 4 sequential items of array                                                                                                                                                           |
| 269   | 0200     |              |                                                                                                                                                                                       |
| 26A   | 225F     |              |                                                                                                                                                                                       |
| 26B   | C257     |              |                                                                                                                                                                                       |


## Description

We store array of four integers at cells 0x268 - 0x26B. Value of **`array_st_pointer`** is address of first array item and **`array_curr_pointer`** store address of processing item. Value of **`loop_counter`** uses for loop and equals to array size. At loop body (0x25D - 0x264) we get next array value, check if its last bit equals to 1 by ROR and BCS commands and skip loop body if it is not. And then we load **`result`**, increment and store again.

So, that program gets count of odd array elements

## Data representation and available values

### Input:

**`array_st_pointer`** (0x253), **`array_curr_pointer`** (0x254) - array items addresses. Depends on array position (0x268 - 0x26B for us) can be from 0x000 to 0x7FF cause there 2048 data cells.                                                                                                 

**`loop_counter`** (0x255) - count of loop cycles. Integer, for our program is 4, but array theoretically can store (2048 - 22) = 2026 elements (memory size minus program size)                                             

> **`array_st_pointer`** and **`loop_counter`** have not necessarily be first element and whole array size. We can tune that values fo getting slice of array
 
array (0x268 - 0x26B) - Sequential stored items of array. Can be signed integers, for example, from -32768 to 32767

### Output:

**`result`** (0x256) - count of odd elements in array. Integer from 0 to 65535


## Assembly
[Basic computer assembly support for vs code](https://github.com/mamsdeveloper/bcomp-asm)
```bcomp

	                        ORG	                     0x253
array_st_pointer:	        WORD	                 $array
array_curr_pointer:	        WORD	                 ?
loop_counter:	            WORD	                 ?
result:	                    WORD	                 ?
                                         
START:	                    CLA           
	                        ST                       result
	                        LD                       #4
                            ST                       loop_counter
	                        LD                       array_st_pointer
	                        ST                       array_curr_pointer
loop_body:	                LD	                     (array_curr_pointer)+
                                               
	                        BCC	                     loop_end
	                        ROL                  
	                        LD	                     result
	                        INC                  
	                        ST	                     result
loop_end:	                LOOP	                 loop_counter
	                        JUMP	                 loop_body
	                        HLT
                                    
	                        ORG	0x268
array:	                    WORD	                0x0280, 0x0200, 0x225F, 0xC257

```