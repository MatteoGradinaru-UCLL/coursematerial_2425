# write your code here
def parse_day(string):
    return int(string[:2])

def parse_month(string):
    return int(string[3:5])

def parse_year(string):
    return int(string[6:])

print(parse_day("01/02/2000"))
print(parse_month("01/02/2000"))
print(parse_year("01/02/2000"))