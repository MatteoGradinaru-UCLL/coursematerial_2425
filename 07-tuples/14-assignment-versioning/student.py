# write your code here
def increase_version(version, breaking_change, new_features):

    major, minor, patch = version

    if breaking_change == True:
        major += 1
        minor = 0
        patch = 0
    
    elif breaking_change == True and new_features == True:
        major += 1
        minor = 0
        patch = 0 

    elif breaking_change == False and new_features == True:
        minor += 1
        patch = 0

    else:
        patch += 1

    return major, minor, patch
print(increase_version((1, 2, 3), breaking_change=False, new_features=True))


def is_more_recent(v1, v2):

    if v1 > v2:
        return True
    else:
        return False
print(is_more_recent((1, 2, 3), (1, 2, 4)))


def is_older(v1, v2):

    if v1 < v2:
        return True
    else:
        return False
print(is_more_recent((1, 2, 3), (1, 2, 4)))