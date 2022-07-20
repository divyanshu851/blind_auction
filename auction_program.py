from pickle import HIGHEST_PROTOCOL
from logo import logo
import os
print(logo)
print("Welcome to the secret auction program ")

bidder = {}

bid_continue = True
while bid_continue:
    name = input("What is your name : ")
    bid = int(input("What's your bid : $"))
    other_bidder = input("Are there any other bidders ? Type 'yes' or 'no' :")

    bidder[name] = bid
    if other_bidder == 'yes':
        bid_continue = True
        os.system('cls')
    else:
        bid_continue = False
    
for key in bidder:
    highest = 0
    winner = ''
    bid_value = bidder[key]
    if bid_value > highest:
        highest = bid_value
        winner = key

print(f'The winner is {winner} with ${highest}')
    