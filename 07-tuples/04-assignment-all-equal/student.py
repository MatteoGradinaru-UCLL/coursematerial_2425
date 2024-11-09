# write your code here
def all_equal(xs):
    for i in range(len(xs)-1):
        if xs[i] != xs[i+1]:
            return False   
    return True
print(all_equal((1, 1, 5, 2)))
           