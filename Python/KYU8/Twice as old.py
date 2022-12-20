def twice_as_old(dad_years_old, son_years_old):

    age_at_birth = dad_years_old - son_years_old
    twice = age_at_birth * 2

    if dad_years_old >= twice:
        return dad_years_old - twice
    else:
        return twice - dad_years_old


if __name__ == "__main__":
    assert twice_as_old(36, 7) == 22
    assert twice_as_old(55, 30) == 5
    assert twice_as_old(42, 21) == 0
    assert twice_as_old(22, 1) == 20
    assert twice_as_old(29, 0) == 29
