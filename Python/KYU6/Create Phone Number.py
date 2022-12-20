def create_phone_number(n):
    len(n) == 10

    prefix = ("")
    after_prefix = ("")
    final = ("")

    for i in n:
        n.count(i)
        if len(prefix) != 3:
            prefix += str(i)
            continue
        if len(after_prefix) != 3:
            after_prefix += str(i)
            continue
        if len(final) != 4:
            final += str(i)
            continue

    phone_number = "(" + prefix + ")" + " " + after_prefix + "-" + final
    return phone_number


if __name__ == "__main__":
    assert create_phone_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert create_phone_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number(
        [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
    assert create_phone_number(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
