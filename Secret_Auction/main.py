import art

print(art.logo)
bidders = {}


def bid_now(bidder, bid):
    bidders[bidder] = bid


def calculate(dictionary_of_bidders):
    highest_bid = 0
    for bidder in dictionary_of_bidders:
        bid_amount = dictionary_of_bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} by bidding the amount of {highest_bid}$! ")
    print(f"Congratulations {winner}")


def main():
    bidder = ""
    bid = 0
    end = False

    print("Welcome to the secret auction program.")
    while not end:

        bidder = input("What is your name?: ")
        bid = int(input("What's your bid?: "))
        bid_now(bidder, bid)
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'").lower()
        if should_continue == 'no':
            end = True
            calculate(bidders)
        elif should_continue == "yes":
            continue

    print(bidders)


main()
