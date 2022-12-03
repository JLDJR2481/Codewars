def first_n_smallest(arr, n):
    if n == 0:
        return []

    new_list = []
    arr_copied = arr.copy()
    arr.sort()
    arr_objective = arr[0:n]
    arr_objective_len = len(arr[0:n])

    new_list_len = 0
    while new_list_len < arr_objective_len:
        for i in arr_copied:
            same_amount = arr_objective.count(i) == new_list.count(i)
            if new_list_len == arr_objective_len:
                break
            if i in arr_objective and not same_amount:
                new_list.append(i)
                new_list_len += 1

    return new_list


if __name__ == "__main__":
    assert first_n_smallest([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert first_n_smallest([5, 4, 3, 2, 1], 3) == [3, 2, 1]
    assert first_n_smallest([1, 2, 3, 1, 2], 3) == [1, 2, 1]
    assert first_n_smallest([1, 2, 3, -4, 0], 3) == [1, -4, 0]
    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []
    assert first_n_smallest([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert first_n_smallest([1, 2, 3, 4, 2], 4) == [1, 2, 3, 2]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 2) == [2, 1]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 3) == [2, 1, 2]
    assert first_n_smallest([-3, -10, -8, -8, 4, -7, -10, -8, -6, -6, -
                            9, -10, -10, -4, -5, -6], 7) == [-10, -8, -8, -10, -9, -10, -10]
