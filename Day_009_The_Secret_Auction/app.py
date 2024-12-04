# Creating the Secret Auction Program 

from art import logo
import os

# Clearing the Screen
print(logo)

other_bidders = True
players = {}

while other_bidders is True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    question = input("Are there any other bidders? Type 'yes or 'no'.")
    players[name] = bid
    os.system('cls')
    print(logo)
    if question == "no":
        other_bidders = False
        highest_bidder = max(players, key=players.get)
        print(f"The winner is {highest_bidder} with a bid of ${players[highest_bidder]}")