def how_much_i_love_you(nb_petals):
    petals = (nb_petals % 6)
    
    if petals == 1 :
        return "I love you"
    
    elif petals == 2 :
        return "a little"
    
    elif petals == 3 :
        return "a lot"
    
    elif petals == 4 :
        return "passionately"
    
    elif petals == 5 :
        return "madly"
    
    elif petals == 0 :
        return "not at all"
    
if __name__ == "__main__":
    assert how_much_i_love_you(7) =="I love you"
    assert how_much_i_love_you(3) =="a lot"
    assert how_much_i_love_you(6) =="not at all" 