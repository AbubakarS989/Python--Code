#  In this project .I added a feature to increase bid if the user want 

from art_AuctionP import logo
import os


def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def find_higher_bidder(bidding_records):
    """
    Finds the highest bidder(s) and displays the winner(s) with their bids.

    Args:
        bidding_records (dict): A dictionary containing bidders as keys and their corresponding bids as values.
    """
    highest_bid = 0
    winners = []
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winners = [bidder]
        elif bid_amount == highest_bid:
            winners.append(bidder)

    if len(winners) == 1:
        print(f"The winner is {winners[0]} with a bid of {highest_bid}$")
    else:
        print("It's a tie! The winners are:")
        for i, winner in enumerate(winners, start=1):
            print(f" {i} - {winner}")


# Program starts here

print(logo)

bids = {}
bidding_finished = False
while not bidding_finished:
    print("Welcome to the Secret Auction Program Instructions")
    name = input("What is your name?: ")
    price = int(input("What is your bid?$: "))
    bids[name] = price

    if name in bids:
        current_bid = bids[name]
    print(f"Your current bid is {current_bid}")
    choice = input("Do you want to increase your bid? Type 'Yes' or 'No': ").lower()

    if choice == "yes":
        add_bid = int(input("How much do you want to increment your bid?$: "))
        bids[name] = current_bid + add_bid
    elif choice == "no":
        pass
    else:
        print("Invalid choice. Type 'Yes' or 'No'.")

    other_bidders = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
    if other_bidders == "no":
        bidding_finished = True
        find_higher_bidder(bids)
    elif other_bidders == "yes":
        clear_console()

