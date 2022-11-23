def duplicate_encode(string):

    string = string.upper()

    words = {}
    for letter in string:
        if letter not in words:
            words[letter] = '('
        else:
            words[letter] = ')'

    result = ""
    for letter in string:
        result += words[letter]

    return result


if __name__ == "__main__":

    assert  duplicate_encode("din") == "((("
    assert  duplicate_encode("recede") == "()()()"
    assert  duplicate_encode("Success") == ")())())"
    assert  duplicate_encode("(( @") == "))(("