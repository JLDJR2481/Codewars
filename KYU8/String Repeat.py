def repeat_str(repeat, string):
    return string * repeat  

if __name__ == "__main__":

    assert repeat_str(4, 'a') == 'aaaa'
    assert repeat_str(3, 'hello ') == 'hello hello hello '
    assert repeat_str(2, 'abc') == 'abcabc'