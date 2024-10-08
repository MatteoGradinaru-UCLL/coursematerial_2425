# write your code here
from math import floor, ceil

def hours(duration):
    h = 3600
    return floor (h//3600)
print (hours(3600))


def minutes(duration):
    
    return floor (duration//60)
print (minutes(3600))


def seconds(duration):
    return floor (duration//60)
print (seconds(3600))