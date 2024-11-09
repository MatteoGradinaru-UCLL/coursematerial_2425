# write your code here
def split_in_two(xs):

    split = (len(xs)+1) // 2

    left = xs[:split]
    right = xs[split:]

    return left, right

print(split_in_two((1, 2, 3, 4)))