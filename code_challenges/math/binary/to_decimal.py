def to_decimal(binary_number: str):
    binary_list = list(binary_number)
    decimal_number: int = 0
    position: int = 0
    while binary_list:
        digit: str = binary_list.pop()
        multiplier: int = 2 ** position
        decimal_number += int(digit) * multiplier
        position += 1
    return decimal_number
