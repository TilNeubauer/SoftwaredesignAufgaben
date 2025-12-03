import math

# This module contains 3 fkt for calulation for the date 
#
# check_leap_yaer():
#   checks if a year is a leap year
#
# day_of_date():
#   returns the weekday of any date 
#
# week_in_year():
#   returns the current week number of the year (follow the ISO-8601 standard)



def check_leap_yaer(year: int) -> bool:
    # This fkt checks if a year is a leap year
    #
    # year: int | year you want check
    #
    # return: bool | True leap year | False not a leap year


    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def day_of_date(d: int, m: int, y: int) -> int:
    # fkt returns the weekday of any date
    # The fkt works as far back as 1753, for dates before that it doesn't work
    #
    # d: int | day of the date 
    # m: int | month of the date 
    # y: int | year of the date 
    #
    # return: int | 1: Mondy, 2: Tuesday, ..., 7: Sunday
    #             | -1: if enterd value isn't coreckt or day can't be calulated

    dict_month_key = {'1' : 1,
                      '100' : 0, # 1 in leap year
                      '2' : 4,
                      '200' : 3, # 2 in leap year
                      '3' : 4,
                      '4' : 0,
                      '5' : 2,
                      '6' : 5,
                      '7' : 0,
                      '8' : 3,
                      '9' : 6,
                      '10' : 1,
                      '11' : 4,
                      '12' : 6
                      }
    
    if y < 1753:
        return -1

    if y < 2000:
        y_re = y % 2000
    elif y >= 1000:
        y_re = y % 1000
    else:
        return -1
    
    if m < 3:
        if check_leap_yaer(y):
            m *= 100

    first_sum = y_re + int(y_re/4) + d + dict_month_key[str(m)]

    if y < 1800:
        first_sum += 4
    elif y < 1900:
        first_sum += 2
    elif y >= 2000 and y < 2100:
        first_sum -= 1

    day_shifted = first_sum % 7 
    day = day_shifted - 1
    if day < 1:
        day += 7

    return day


def week_num(d: int, m: int, y: int) -> int:
    # returns the current week number of the year (follow the ISO-8601 standard)
    #
    # d: int | day of the date 
    # m: int | month of the date 
    # y: int | year of the date 
    #
    # return: int | retuns the number of week from beginnig of the year



    dict_days_month = {'1' : 31,
                      '2' : 28,
                      '3' : 31,
                      '4' : 30,
                      '5' : 31,
                      '6' : 30,
                      '7' : 31,
                      '8' : 31,
                      '9' : 30,
                      '10' : 31,
                      '11' : 30,
                      '12' : 31
                      }

    day_11x = day_of_date(1, 1, y) - 1 # -1 bacause monday = 0

    days_passed = 0
    for e in range(1,m):
        days_passed += dict_days_month[str(e)]
    if m > 1 and check_leap_yaer(y):
        days_passed += 1
    days_passed += d

    week_number = math.floor((days_passed + day_11x) / 7) + 1

    return week_number