# write your code here
def passing_percentage(grades):

    count = 0

    for i in grades:
        if i >= 10:
            count += 1

    percentage = (count / len(grades)) * 100

    return percentage

print(passing_percentage((20, 20)))