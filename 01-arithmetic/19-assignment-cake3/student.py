# write your code here
def cake3(eggs, flour, butter, sugar):
    return min(eggs//5, flour//250, butter//200, sugar//250)
print(cake3(5, 250, 300, 400))