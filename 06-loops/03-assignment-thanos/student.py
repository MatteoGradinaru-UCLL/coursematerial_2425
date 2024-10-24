# write your code here
def thanos(queue_size, target_size):
    
    snaps = 0

    while queue_size > target_size:
        snaps += 1
        queue_size = queue_size / 2 
    return snaps

print(thanos(8, 3))