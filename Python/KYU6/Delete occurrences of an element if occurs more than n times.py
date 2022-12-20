def delete_nth(order, max_e):

    result = []

    for i in order:
        if i not in result:
            result.append(i)

        elif i in result:
            result.count(i)
            if result.count(i) < max_e:
                result.append(i)
            elif result.count(i) == max_e:
                continue
    return result


if __name__ == "__main__":
    assert delete_nth([20, 37, 20, 21], 1) == [20, 37, 21]
    assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [
        1, 1, 3, 3, 7, 2, 2, 2]
