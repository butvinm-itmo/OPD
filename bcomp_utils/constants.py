ATTRS_COMMANDS = {
    '2': ('AND', 'M & AC -> AC'),
    '3': ('OR', '^(^M & ^AC) -> AC'),
    '4': ('ADD', 'M + AC -> AC'),
    '5': ('ADC', 'M + AC + C -> AC'),
    '6': ('SUB', 'AC - M -> AC'),
    '7': ('CMP', 'Set flags by result of AC - M'),
    '8': ('LOOP', 'M - 1 -> M; IF M <= 0 THEN IP + 1 -> IP'),
    '9': ('NONE', 'Reserve'),
    'A': ('LD', 'M -> AC'),
    'B': ('SWAM', 'M <-> AC'),
    'C': ('JUMP', 'M -> IP'),
    'D': ('CALL', 'SP - 1 -> SP; IP -> SP; M -> IP'),
    'E': ('ST', 'AC -> M'),
}

NO_ATTR_COMMANDS = {
    '0000': ('NOP', 'Debug point'),
    '0100': ('HLT', 'Disable Tacts Generator, switch to Manual Mode'),
    '0200': ('CLA', '0 -> AC'),
    '0280': ('NOT', '^AC -> AC'),
    '0300': ('CLC', '0 -> C'),
    '0380': ('CMC', '^C -> C'),
    '0400': ('ROL', 'AC and C rolls to left: AC_15 -> C, C -> AC_0'),
    '0480': ('ROR', 'AC and C rolls to right: AC_0 -> C, C -> AC_15'),
    '0500': ('ASL', 'AC roll to left: AC_15 -> C, 0 -> AC_0'),
    '0580': ('ASL', 'AC roll to right: AC_0 -> C, AC_15 -> AC_14'),
    '0600': ('SXTB', 'AC_7 -> AC_15...AC_8'),
    '0680': ('SWAB', 'AC_7...AC_0 <-> AC_15...AC_8'),
    '0700': ('INC', 'AC + 1 -> AC'),
    '0740': ('DEC', 'AC - 1 -> AC'),
    '0780': ('NEG', '^AC + 1 -> AC'),
    '0800': ('POP', '(SP)+ -> AC'),
    '0900': ('POPF', '(SP)+ -> PS'),
    '0A00': ('RET', '(SP)+ -> IP'),
    '0B00': ('IRET', '(SP)+ -> PS, (SP)+ -> IP'),
    '0C00': ('PUSH', 'AC -> -(SP)'),
    '0D00': ('PUSHF', 'PS -> -(SP)'),
    '0E00': ('SWAP', 'AC <-> (SP)'),
}

BRANCHING_COMMANDS = {
    'F0': ('BEQ', 'IF Z==1 THEN IP + D + 1 -> IP'),
    'F1': ('BNE', 'IF Z==0 THEN IP + D + 1 -> IP'),
    'F2': ('BMI', 'IF N==1 THEN IP + D + 1 -> IP'),
    'F3': ('BPL', 'IF N==0 THEN IP + D + 1 -> IP'),
    'F4': ('BCS', 'IF C==1 THEN IP + D + 1 -> IP'),
    'F5': ('BCC', 'IF C==0 THEN IP + D + 1 -> IP'),
    'F6': ('BVS', 'IF V==1 THEN IP + D + 1 -> IP'),
    'F7': ('BVC', 'IF V==0 THEN IP + D + 1 -> IP'),
    'F8': ('BCS', 'IF N xor V == 1 THEN IP + D + 1 -> IP'),
    'F9': ('BCC', 'IF N xor V == 0 THEN IP + D + 1 -> IP'),
    'CE': ('BR', 'IP + D + 1')
}


IO_COMMANDS = {
    '10': ('DI', 'Disable interrupts'),
    '11': ('EI', 'Enable interrupts'),
    '12': ('IN', 'REG -> AC'),
    '13': ('OUT', 'AC -> REG'),
    '18': ('INT', 'Interrupt with vector NUM'),
    '0B': ('IRET', '(SP)+ -> PS; (SP)+ -> IP')
}
