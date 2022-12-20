def people_with_age_drink(age):
    age >= 0
    
    if age <14:
        return 'drink toddy'
    
    elif age >= 14 and age < 18:
        return 'drink coke'
    elif age >= 18 and age < 21:
        return 'drink beer'
    else:
        return 'drink whisky'
    
if __name__ == "__main__":

    assert people_with_age_drink(13) == 'drink toddy'
    assert people_with_age_drink(0) == 'drink toddy'
    
    assert people_with_age_drink(17)  == 'drink coke'
    assert people_with_age_drink(15) == 'drink coke'
    assert people_with_age_drink(14) == 'drink coke'
        
    assert people_with_age_drink(22) == 'drink whisky'
    assert people_with_age_drink(21) == 'drink whisky'