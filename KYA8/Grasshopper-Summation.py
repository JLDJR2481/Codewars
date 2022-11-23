def summation(num):
    
    return sum(range(num+1))

if __name__ == "__main__":
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791 