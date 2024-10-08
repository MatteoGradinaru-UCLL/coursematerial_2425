# write your code here
from math import floor, ceil

def candy_per_child(candy_count, child_count):
    return floor (candy_count/child_count)
print(candy_per_child(11, 5))