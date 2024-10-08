# write your code here
def is_valid_month(month):
    return month >= 1 and month <= 12

def is_leap_year(year):
    return (year%4 == 0 and year%100 != 0) or year%400 == 0

def has_30_days(month):
    return month == 4 or month == 6 or month == 9 or month == 11

def has_31_days(month):
    return month == 1 or  month == 3 or  month == 5 or  month == 7 or  month == 8 or  month == 10 or  month == 12

def has_28_days(month, year):
    return month == 2 and is_leap_year(year) != 1

def has_29_days(month, year):
    return month == 2 and is_leap_year(year) == 1

def is_valid_day(day, month, year):
    return (day >= 1 and day <=30 and has_30_days(month)) or (day >= 1 and day <=31 and has_31_days(month)) or (day >= 1 and day <=29 and has_29_days(month, year)) or (day >= 1 and day <=28 and has_28_days(month,year))

def is_valid_date(day, month, year):
    return is_valid_month(month) == 1 and is_valid_day(day,month,year) == 1 and year>0
print(is_valid_date(1, 18, 2008))