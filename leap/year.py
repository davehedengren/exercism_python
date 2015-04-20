def is_leap_year(year):
    #leap years are divisable by 4
    if year % 4 == 0:
        # except when they are divisible by 100
        if year % 100 == 0:
            #unless they are divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
