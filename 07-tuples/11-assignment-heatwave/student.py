# write your code here
def heatwave(temperatures):

    count_25 = 0
    count_30 = 0

    for i in temperatures:
        if i >= 25:
            count_25 += 1
            
            if i >= 30:
                count_30 += 1

            
            if count_25 >= 5 and count_30 >= 3:
                return True
        else:

            count_25 = 0
            count_30 = 0

    return False

print(heatwave((40, 40, 40, 40, 40)))