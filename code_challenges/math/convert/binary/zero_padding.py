def pad(binary_number: str, to: int):
    binary, places = binary_number, to
    binary_len = len(binary)
    if binary_len > places:
        raise ValueError("No zero-padding")
    missing_places = places - binary_len
    missing_string = missing_places * "0"
    new_binary = missing_string + binary
    return new_binary
