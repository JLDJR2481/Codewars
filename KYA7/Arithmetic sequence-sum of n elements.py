def arithmetic_sequence_sum(a, r, n):
    result = a
    count = 1
    while count < n:
        result += a + (count * r)
        count += 1
    return result

if __name__ == "__main__":

    assert arithmetic_sequence_sum(3, 2, 20) == 440
    assert arithmetic_sequence_sum(2, 2, 10) == 110
    assert arithmetic_sequence_sum(1, -2, 10) == -80