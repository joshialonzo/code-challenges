from code_challenges.math.primes.prime import is_prime


def test_is_prime_1():
    number = 1
    assert not is_prime(number)


def test_is_prime_2():
    number = 2
    assert is_prime(number)


def test_is_prime_3():
    number = 3
    assert is_prime(number)


def test_is_prime_4():
    number = 4
    assert not is_prime(number)


def test_is_prime_5():
    number = 5
    assert is_prime(number)


def test_is_prime_7():
    number = 7
    assert is_prime(number)


def test_is_prime_25():
    number = 25
    assert not is_prime(number)
