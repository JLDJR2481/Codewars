def mouth_size(animal):

    if animal.lower() == "alligator":
        return 'small'
    else:
        return 'wide'


if __name__ == "__main__":
    assert mouth_size("toucan") == "wide"
    assert mouth_size("ant bear") == "wide"
    assert mouth_size("alligator") == "small"
