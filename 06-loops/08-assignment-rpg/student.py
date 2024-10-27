def rpg2(n_sides, goal):
    percentage = 0
    for i in range(1,n_sides+1):
        for t in range(1,n_sides+1):
            combinations = i + t
            if combinations >= goal:
                percentage += (100/((n_sides)**2))
    return percentage
print(rpg2(4, 5))

def rpg3(n_sides, goal):
    percentage = 0
    for i in range(1,n_sides+1):
        for c in range(1,n_sides+1):
            for t in range(1,n_sides+1):
                combinations = i + c + t
                if combinations >= goal:
                    percentage += (100/((n_sides)**3))
    return percentage