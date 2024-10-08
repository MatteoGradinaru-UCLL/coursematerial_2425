# write your code here
def earlier(h1, m1, h2, m2):
    return (h1 < h2) or (h1 == h2 and m1 < m2)
print(earlier(1, 2, 3, 4))
