# write your code here
def domino_chain(dominos):

    for i in range(len(dominos)-1):
        if dominos[i][1] != dominos[i+1][0]:
            return False
    return True

print(domino_chain(((1, 2), (2, 5), (5, 3), (3, 3), (3, 0))))