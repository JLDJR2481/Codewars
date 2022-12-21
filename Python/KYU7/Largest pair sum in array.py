def largest_pair_sum(numbers):
    numbers = sorted(numbers, reverse=True)

    return numbers[0] + numbers[1]


if __name__ == "__main__":
    print('Testing')
    assert largest_pair_sum([10, 14, 2, 23, 19]) == 42
    assert largest_pair_sum([-100, -29, -24, -19, 19]) == 0
    assert largest_pair_sum([1, 2, 3, 4, 6, -1, 2]) == 10
    assert largest_pair_sum([-10, -8, -16, -18, -19]) == -18
    print('Success')
