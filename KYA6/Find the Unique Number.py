def find_uniq(arr):

    if arr.count(max(arr)) == 1:
        return max(arr)
    else:
        return min(arr)
    
if __name__ == "__main__":
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10