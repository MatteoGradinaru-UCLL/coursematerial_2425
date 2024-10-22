# write your code here
def parse_position_x(string):
    
    x_and_y = string[1:-1] 
    komma_position = x_and_y.find(",")
    x_position = x_and_y[:komma_position]

    return float(x_position)
print(parse_position_x("(12.453, 9.120)"))



def parse_position_y(string):

    x_and_y = string[1:-1] 
    komma_position = x_and_y.find(",")
    y_position = x_and_y[komma_position+2:]

    return float(y_position)
print(parse_position_y("(12.453, 9.120)"))