def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


if __name__ == "__main__":

    assert to_camel_case("") == ""
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"
