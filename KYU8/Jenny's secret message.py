def greet(name):
    if name != "Johnny":
        return "Hello, " + name +"!"
    if name == "Johnny":
        return "Hello, my love!"

if __name__ == "__main__":

    assert greet("James") == "Hello, James!"
    assert greet("Jane") == "Hello, Jane!"
    assert greet("Jim") == "Hello, Jim!"

    assert greet("Johnny") == "Hello, my love!"