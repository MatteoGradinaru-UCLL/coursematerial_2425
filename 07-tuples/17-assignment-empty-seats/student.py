# write your code here
def empty_seats(used_seats):

    empty = 0

    for i in range(1, len(used_seats)):

        gap = used_seats[i] - used_seats[i-1] - 1
        empty += gap
    
    return empty

print(empty_seats((1, 3)))