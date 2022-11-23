def is_prime(num):

    divisor = 2

    while divisor < num and num % divisor != 0:
        divisor += 1

    if divisor == num:
        return True
    return False


def sexy_prime(x, y):

    return is_prime(x) and is_prime(y) and (x - y == 6 or y - x == 6)

if __name__ == "__main__":
    assert sexy_prime(5, 11) == True
    assert sexy_prime(13, 19) == True
    assert sexy_prime(83, 89) == True
    assert sexy_prime(1, 11) == False