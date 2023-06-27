def get_relative_address(str_address: str, str_offset: str) -> str:
    address = int(str_address, 16)
    offset = int(str_offset, 16)
    if offset > 0x7FFFFFFF:
        offset -= 0x100000000

    return str(hex(address + offset + 1))


if __name__ == "__main__":
    var = {
        '0xea': 'E',
        '0xe9': 'A',
        '0xe8': 'B',
        '0xe7': 'C',
    }
    while True:
        # Get the address and offset
        address, offset = input("Enter the address and offset: ").split()

        # Get the relative address
        relative_address = get_relative_address(address, offset)

        # Print the relative address
        print(relative_address)
        