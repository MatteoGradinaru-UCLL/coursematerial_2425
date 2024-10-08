# write your code here
def higher_card(card1, card2):
    return (card1 == 1 and card2 !=1) or (card1 != 1 and card2 !=1 and card1 > card2)
print(higher_card(5, 2))