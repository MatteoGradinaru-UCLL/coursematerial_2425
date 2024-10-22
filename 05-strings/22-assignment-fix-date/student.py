# write your code here
def fix_date(date):
    month = date[:2]
    day = date[3:5]
    year = date[6:]

    new_date = year + "/" + month + "/" + day

    return new_date
print(fix_date("10/19/2024"))