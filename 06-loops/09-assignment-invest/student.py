def invest(amount, rate, goal):
    year = 0

    while amount < goal:
        year += 1
        amount += (amount * rate)/100
    return year

print(invest(100, 100, 1000))
