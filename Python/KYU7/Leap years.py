def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
        
    elif year % 400 == 0:
        return True
    
    else:
        return False
    
if __name__ == "__main__":
   
   assert isLeapYear(1984) == True
   assert isLeapYear(2000) == True 

   assert isLeapYear(1234) == False
   assert isLeapYear(1100) == False 