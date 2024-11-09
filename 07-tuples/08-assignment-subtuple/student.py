# write your code here
def subtuple(xs, ys):
    
    if ys == None:
        return True
    
    for i in range(len(xs) - len(ys) +1):
        if xs[i:i + len(ys)] == ys:
            return True
    return False

print(subtuple((1, 2, 3, 4, 5), (1, 3, 4)))