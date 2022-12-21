def human_years_cat_years_dog_years(human_years):

    humanYears = 1
    catYears = 0
    dogYears = 0
    while humanYears <= human_years:
        if humanYears == 1:
            catYears += 15
            dogYears += 15
            humanYears += 1
        elif humanYears == 2:
            catYears += 9
            dogYears += 9
            humanYears += 1
        elif humanYears >= 3:
            catYears += 4
            dogYears += 5
            humanYears += 1

    return [human_years, catYears, dogYears]


if __name__ == "__main__":
    print('Testing')
    assert human_years_cat_years_dog_years(1) == [1, 15, 15]

    assert human_years_cat_years_dog_years(2) == [2, 24, 24]

    assert human_years_cat_years_dog_years(10) == [10, 56, 64]
    print('Success')
