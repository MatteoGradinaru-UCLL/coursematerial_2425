# write your code here
def greet(name):
    return f"Hello, {name}!"


def interactive_greet():

    name = input("What is your name? ")
    return (greet(name))

print(interactive_greet())