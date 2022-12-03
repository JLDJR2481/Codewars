def greet(name, owner):
    
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

if __name__ == "__main__":
        
    assert greet('Daniel', 'Daniel') == 'Hello boss' 
    assert greet('Greg', 'Daniel') == 'Hello guest'