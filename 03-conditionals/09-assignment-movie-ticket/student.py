# write your code here
from math import ceil 
def movie_ticket(duration, imax, student, ticket_count):

    if duration <= 90:
        ticket_price = 10
    elif duration <= 120:
        ticket_price = 11
    elif duration <= 150:
        ticket_price = 12
    else: ticket_price = 15

    if imax :
        ticket_price = ceil(ticket_price * 1.20)

    if student:
        ticket_price -= 3

    total_price = ticket_price * ticket_count

    return total_price
print(movie_ticket(70, False, False, 1))