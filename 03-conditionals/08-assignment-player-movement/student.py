# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    
    if left_arrow and right_arrow:
        return position
    
    movement = 2 if shift else 1

    if left_arrow:
        position -= movement
    elif right_arrow:
        position += movement

    return position
print(player_movement(10, True, False, False)) 