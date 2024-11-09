# write your code here
def increasing(ns):

    for i in range(1, len(ns)):
        if ns[i] < ns[i - 1]:
            return False
    return True

print(increasing((1, 2, 4, 3)))