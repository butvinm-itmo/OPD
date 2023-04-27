a = int(input(), 16)
if a >= 0xf000:
    a = a - 0xffff

print(a)