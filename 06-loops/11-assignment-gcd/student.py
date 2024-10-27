def gcd(x, y):
    x = abs(x)
    y = abs(y)
    
    min_value = min(x, y)

    for i in range(min_value, 0, -1):
        if x % i == 0 and y % i == 0:
            return i

print(gcd(15, 10))