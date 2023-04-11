def is_prime(number):
    if number == 1:
        return False
    counter = 1
    for i in range(2, number + 1):
        if number % i == 0:
            counter += 1
        if counter > 2:
            return False
    return True
