def merge(*dicts):
    r={}
    for d in dicts:
        for k in d:
            r[k]=r.get(k,[])+[d[k]]
    return r

if __name__ == "__main__":
    assert merge({},{},{}) == {}

    assert merge({"A": 1, "B": 2, "C": 3}) == {"A": [1], "B": [2], "C": [3]}


    assert merge({"A": 1}, {"B": 2}) == {"A": [1], "B": [2]}


    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}) == {"A": [1, 4], "B": [2], "C": [3], "D": [5]}