from random import choices, randint


def int_to_8bit_hex(a: int) -> str:
    if a < -128 or a > 127:
        raise ValueError("Integer must be between -128 and 127.")

    if a < 0:
        a = 256 + a

    return hex(a)[2:].zfill(2)


def int_to_16bit_hex(a: int) -> str:
    if a < -32768 or a > 32767:
        raise ValueError("Integer must be between -32768 and 32767.")

    if a < 0:
        a = 65536 + a

    return hex(a)[2:].zfill(4)


def gen_test(count: int = 10) -> str:
    a_s = choices(range(-128, 128), k=count)
    b_s = choices(range(-128, 128), k=count)

    r_words = []
    tests = []
    for a, b, i in zip(a_s, b_s, range(count)):
        r = a * b

        a_hex = int_to_8bit_hex(a)
        b_hex = int_to_8bit_hex(b)
        r_hex = int_to_16bit_hex(r)
        n, z, v = r < 0, r == 0, abs(r) > 32768

        r_words.append(f'r{i}: word 0x{r_hex}')

        tests.append(f'''ld #0x{a_hex} ; {a} * {b} = {r}
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
        pass{i}:''')

    r_words_block = '\n'.join(r_words)
    tests_block = '\n'.join(tests)

    last_addr = len(r_words) + len(tests) * 9 + 16
    last_addr_hex = int_to_16bit_hex(last_addr)

    return f'''org 0x010
    {r_words_block}

    start:
    {tests_block}

    org 0x{last_addr_hex}
    ld #0x0
    hlt'''.replace('    ', '')


def gen_incorrect_test(count: int = 10) -> str:
    a_s = choices(range(-128, 128), k=count)
    b_s = choices(range(-128, 128), k=count)

    r_words = []
    tests = []
    for a, b, i in zip(a_s, b_s, range(count)):
        r = a * b

        a_hex = int_to_8bit_hex(a)
        b_hex = int_to_8bit_hex(b)
        r_hex = int_to_16bit_hex(r + randint(0, 255))
        n, z, v = not r < 0, not r == 0, not abs(r) > 32768

        r_words.append(f'r{i}: word 0x{r_hex}')

        tests.append(f'''ld #0x{a_hex} ; {a} * {b} = {r}
        word 0x9f{b_hex}
        test_flags{i}:
            test_n{i}: {"bns" if n else "bnc"} fail{i} ; n = {n}
            test_z{i}: {"bns" if n else "bnc"} fail{i} ; z = {z}
        test_result{i}:
            cmp $r{i}
            beq fail{i}
            jump pass{i}
        fail{i}:
            ld #0x1
            hlt
        pass{i}:''')

    r_words_block = '\n'.join(r_words)
    tests_block = '\n'.join(tests)

    last_addr = len(r_words) + len(tests) * 9 + 16
    last_addr_hex = int_to_16bit_hex(last_addr)

    return f'''org 0x010
    {r_words_block}

    start:
    {tests_block}

    org 0x{last_addr_hex}
    ld #0x0
    hlt'''.replace('    ', '')


def check_size(test: str) -> int:
    lines = test.split('\n')
    lines = [line for line in lines if not line.startswith(';')]
    lines = [line for line in lines if not line.endswith(':')]
    lines = [line for line in lines if not 'org' in line]
    return len(lines)


if __name__ == '__main__':
    with open('test.basm', 'w') as f:
        tests = gen_test(100)
        print(check_size(tests))
        f.write(tests)

    with open('test_incorrect.basm', 'w') as f:
        tests = gen_incorrect_test(200)
        print(check_size(tests))
        f.write(tests)
