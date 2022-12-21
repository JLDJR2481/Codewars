def derive(coefficient, exponent):

    multiple = str(coefficient * exponent)
    power = str(exponent - 1)

    return (multiple + 'x' + '^' + power)


if __name__ == "__main__":
    print('Testing')
    assert derive(7, 8) == "56x^7"
    assert derive(5, 9) == "45x^8"
    print('Success')
