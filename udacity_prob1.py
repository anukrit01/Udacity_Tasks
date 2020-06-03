def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

#test2 = isLeapYear(2100)
#print(test2)

def daysInMonth(y, m):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    else:
        if m==2:
            if isLeapYear(y) == True:
                return 29
            else:
                return 28
        else:
            return 30

#test3 = daysInMonth(2020, 4)
#print(test3)

def nextDay(y, m, d):
    if d < daysInMonth(y, m):
        return y, m, d+1
    else:
        if m < 12:
            return y, m+1, 1
        else:
            return y+1, 1, 1

#test = nextDay(2012, 12, 29)
#print(test)

def dateIsBefore(y1, m1, d1, y2, m2, d2):
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return True
        if m1 == m2:
            if d1 < d2:
                return True
    return False

#test1 = dateIsBefore(2012, 5, 26, 2012, 5, 27)
#print(test1)   

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    
    assert not dateIsBefore(y2, m2, d2, y1, m1, d1)

    days = 0
    while dateIsBefore(y1, m1, d1, y2, m2, d2):
        y1, m1, d1 = nextDay(y, m, d)
        days += 1
    return days


main_test = daysBetweenDates(2012, 5, 24, 2012, 5, 25)
print(main_test)
