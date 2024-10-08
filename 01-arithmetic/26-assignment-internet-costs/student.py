# write your code here
def internet_costs(duration_in_seconds, cost_per_block):

    seconds_per_block = 360
    blocks_needed = (duration_in_seconds + seconds_per_block - 1) // seconds_per_block 

    internet_costs = blocks_needed * cost_per_block

    return internet_costs
print (internet_costs(361, 0.5))