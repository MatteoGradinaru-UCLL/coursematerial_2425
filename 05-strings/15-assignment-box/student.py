# write your code here
def box(string):
    length = len(string)
    border = "+" + "-" * (length + 2) + "+"
    middle = f"| {string} |"
    return f"{border}\n{middle}\n{border}"
print(box("Put me in the box"))