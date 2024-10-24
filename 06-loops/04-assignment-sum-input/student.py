# write your code here
def sum_input():
    
    prompt = int(input("Eneter integer: "))
    sum = prompt

    while prompt != 0:

        prompt = int(input("Eneter integer: "))
        sum += prompt

    print(f"The sum equals {sum}.")

sum_input()