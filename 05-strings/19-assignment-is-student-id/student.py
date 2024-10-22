# write your code here
def is_digit(char):
    return "0" <= char <= "9"

def is_student_id(string):

    if len(string) != 8:
        return False 

    if string[0] not in ("r", "R", "s", "S"):
        return False
    
    return all(is_digit(char) for char in string[1:])
    
print(is_student_id('r0123456'))