def duplicate_count(text):

    duplicate = 0
    duplicate_list = []
    list_of_letters = []
    low_text = text.lower()

    if len(low_text) == 0:
        return 0

    else:
        for i in low_text:
            low_text.count(i)

            if low_text.count(i) != 1:
                if i not in list_of_letters:
                    duplicate += 0
                    list_of_letters.append(i)

                if i in list_of_letters:
                    if i not in duplicate_list:
                        duplicate += 1
                        duplicate_list.append(i)

                    if i in duplicate_list:
                        duplicate += 0
                        continue

            if low_text.count(i) == 1:
                list_of_letters.append(i)

        return duplicate


if __name__ == "__main__":
    assert duplicate_count("") == 0
    assert duplicate_count("abcde") == 0
    assert duplicate_count("abcdeaa") == 1
    assert duplicate_count("abcdeaB") == 2
    assert duplicate_count("Indivisibilities") == 2
