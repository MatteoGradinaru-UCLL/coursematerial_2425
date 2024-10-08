# write your code here
def middle(a, b, c):
    big = max(a, b, c)
    small = min(a, b, c)
    middle_abc = (a + b + c) - big - small
    return middle_abc

print(middle(1, 18, 8))