def find_prime_factors(number):
    prime_factors = []
    idx = 2
    while idx <= number:
        mod = number % idx
        if mod == 0:
            prime_factors.append(idx)
            number = number // idx
        else:
            idx += 1
    return prime_factors


def main():
    print(24, find_prime_factors(24))
    print(13, find_prime_factors(13))
    print(92, find_prime_factors(92))
    print(128, find_prime_factors(128))


if __name__ == "__main__":
    main()
