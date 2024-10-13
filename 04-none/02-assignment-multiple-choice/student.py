def multiple_choice(right_answer, given_answer):

    
    if right_answer == given_answer:
        total_points = 1
    elif given_answer is None:
        total_points = 0
    else: total_points = -0.2

    return total_points
print(multiple_choice(3, 3))