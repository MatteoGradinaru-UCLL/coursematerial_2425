# write your code here
def tip_calculator():
    total_price = int(input("Enter total price: "))
    tip_percentage = input("Enter tip percentage (default=20): ")

    if tip_percentage == "":
        tip_percentage = 20
    else: 
        tip_percentage = int(tip_percentage)


    return round(total_price * (1+tip_percentage/100))

print (tip_calculator())