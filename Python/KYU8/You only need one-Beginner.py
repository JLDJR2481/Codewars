def check(a, x):

    if x in a:
        return True
    else:
        return False
    
if __name__ == "__main__":

    assert check ([66, 101] ,66) == True
    assert check([78, 117, 110, 99, 104, 117, 107, 115],8) == False
    assert check([101, 45, 75, 105, 99, 107], 107) == True
    assert check([80, 117, 115, 104, 45, 85, 112, 115], 45) == True
    assert check(['t', 'e', 's', 't'], 'e') == True
    assert check(["what", "a", "great", "kata"], "kat") == False
    assert check([66, "codewars", 11, "alex loves pushups"],"alex loves pushups") == True
    assert check(["come", "on", 110, "2500", 10, '!', 7, 15], "Come") == False
    assert check(["when's", "the", "next", "Katathon?", 9, 7], "Katathon?") == True
    assert check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45) == False
    assert check(["anyone", "want", "to", "hire", "me?"], "me?") == True