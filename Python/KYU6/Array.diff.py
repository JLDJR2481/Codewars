def array_diff(a, b):

    result = []

    for i in a:
        if i not in b:
            result.append(i)
        if i in b:
            continue
    return result


if __name__ == "__main__":
    assert array_diff([1, 2], [1]) == [2]
    assert array_diff([1, 2, 2], [1]) == [2, 2]
    assert array_diff([1, 2, 2], [2]) == [1]
    assert array_diff([1, 2, 2], []) == [1, 2, 2]
    assert array_diff([], [1, 2]) == []
    assert array_diff([1, 2, 3], [1, 2]) == [3]
