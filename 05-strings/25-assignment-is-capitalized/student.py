# write your code here
def is_capitalized(string):

    if len(string) == 0:
        return False


    if string[0] == string[0].upper() and string[1:] == string[1:].lower():
        return True
    else:
        return False

print(is_capitalized("Hello"))