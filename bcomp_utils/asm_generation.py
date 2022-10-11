def set_ac(value: hex) -> list[str]:
    """Generate list with asm commands that set value to accumulator

    Args:
        value (hex): str hex value

    Returns:
        list[str]: generated asm code
    """

    _test_ca = 0
    code = ['CLA']

    int_value = int(value, 16)
    bin_value = bin(int_value)[2:]

    for bit in bin_value:
        code += ['ASL']
        _test_ca <<= 1

        if bit == '1':
            code += ['INC']
            _test_ca += 1

    assert _test_ca == int(value, 16), 'Incorrect value. It may be carry or wrong number representation'
    return code


def set_data(address: hex, value: hex) -> list[str]:
    """Generate list with asm commands that set value to address

    Args:
        address (hex): str hex data address
        value (hex): str hex data values

    Returns:
        list[str]: generated acm code
    """

    code = []
    # set value to AC
    code += set_ac(value)
    # set value from AC to address
    int_address = int(address, 16)
    code += [f'ST {int_address}']

    return code


if __name__ == '__main__':
    code = [
        set_data('149', '4149'),
        set_data('14A', '0100'),
        set_data('14B', 'E14B'),
        set_data('14C', '0100'),
        set_data('14D', '0200'),
        set_data('14E', '4149'),
        set_data('14F', '614A'),
        set_data('150', 'E14B'),
        set_data('151', 'A155'),
        set_data('152', '314B'),
        set_data('153', 'E14C'),
        set_data('154', '0100'),
        set_data('155', '0200'),
    ]
    [print(line) for line in code]

    # code_text = '\n'.join(code)
    # with open('data.txt', 'w') as f:
    #     f.write(code_text)
