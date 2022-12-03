def likes(names):

    l_likes = []
    list_for_3 = []

    if names == []:
        return 'no one likes this'
    else:
        for i in names:
            if len(names) == 1:
                l_likes.append(i)
                return ''.join(l_likes) + " likes this"

            if len(names) == 2:
                l_likes.append(i)
                if len(l_likes) != 2:
                    continue
                if len(l_likes) == 2:
                    return ' and '.join(l_likes) + " like this"

            if len(names) == 3:
                if len(l_likes) != 2:
                    l_likes.append(i)
                    continue
                if len(l_likes) == 2:
                    list_for_3.append(i)
                    return ', '.join(l_likes) + " and " + ''.join(list_for_3) + " like this"

            if len(names) >= 4:
                if len(l_likes) != 2:
                    l_likes.append(i)
                    continue
                if len(l_likes) == 2:
                    others = len(names) - len(l_likes)
            return ', '.join(l_likes) + " and " + str(others) + " others like this"


if __name__ == "__main__":
    assert likes([]) == 'no one likes this'
    assert likes(['Peter']) == 'Peter likes this'
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this'
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']
                 ) == 'Alex, Jacob and 2 others like this'
