def to_binary(number):
    binary_string = ""
    numerator = number
    denominator = 2

    while numerator > 0:
        remainder = numerator % denominator
        binary_string = str(remainder) + binary_string

        quotient = numerator // denominator
        numerator = quotient

    return binary_string
