from constants import IO_COMMANDS, ATTRS_COMMANDS, NO_ATTR_COMMANDS, BRANCHING_COMMANDS


def dis(digit: str) -> tuple[str, str]:
    """Convert digit command representation to mnemonic and get description

    Args:
        digit (str): command as 4-digit hex code

    Returns:
        tuple[str, str]: command as COMMAND_NAME (ARGUMENT) and description
    """

    code, arg = digit, ''
    if digit[:2] in IO_COMMANDS:
        mnemonic, description = IO_COMMANDS[digit[:2]]
        if digit[:2] in ('12', '13', '18'):
            code, arg = digit[:2], digit[2:]

    elif digit[:2] in BRANCHING_COMMANDS:
        mnemonic, description = BRANCHING_COMMANDS[digit[:2]]
        code, arg = digit[:2], digit[2:]
        arg = str(int(arg, 16))

    elif digit[0] in ATTRS_COMMANDS:
        mnemonic, description = ATTRS_COMMANDS[digit[0]]
        code, arg = digit[:1], digit[1:]
        arg = str(int(arg, 16))

    elif digit in NO_ATTR_COMMANDS:
        mnemonic, description = NO_ATTR_COMMANDS[digit]
    else:
        raise ValueError(f'Command {digit} was not found')

    command = f'{mnemonic} {arg}'
    return command, description


if __name__ == '__main__':
    for i in range(16**4):
        dc = hex(i)[2:].upper().zfill(4)
        try:
            print(dc, *dis(dc))
        except ValueError as e:
            pass
