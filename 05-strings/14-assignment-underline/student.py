# write your code here
def underline(string):
    dashes = '-' * len(string)
    return f"{string}\n{dashes}"

print(underline("Some String"))