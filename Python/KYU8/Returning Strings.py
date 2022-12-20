def greet(name):

    return "Hello, " + name + " how are you doing today?"


if __name__ == "__main__":
    assert greet('Ryan') == "Hello, Ryan how are you doing today?"
    assert greet('Shingles') == "Hello, Shingles how are you doing today?"
