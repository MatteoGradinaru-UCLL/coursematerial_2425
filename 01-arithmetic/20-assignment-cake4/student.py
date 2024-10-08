# write your code here
def cake4(eggs, flour, butter, sugar, eggs_per_cake,
          flour_per_cake, butter_per_cake, sugar_per_cake):
    
    return min(eggs//eggs_per_cake,flour//flour_per_cake,
               butter//butter_per_cake,sugar//sugar_per_cake)
print (cake4(15, 300, 400, 1000, 5, 200, 100, 50))