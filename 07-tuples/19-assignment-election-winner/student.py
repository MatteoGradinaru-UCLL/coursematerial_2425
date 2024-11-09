# write your code here
def election_winner(votes):

    if not votes:
        return None
       
    sorted_votes = sorted(votes)
    max_count = 0
    current_count = 1
    winner = sorted_votes[0]
    
    
    for i in range(1, len(sorted_votes)):
        if sorted_votes[i] == sorted_votes[i - 1]:
            current_count += 1
        else:
            
            if current_count > max_count:
                max_count = current_count
                winner = sorted_votes[i - 1]
            current_count = 1

    if current_count > max_count:
        winner = sorted_votes[-1]
    
    return winner
