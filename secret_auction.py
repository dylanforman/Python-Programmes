from replit import clear
import art
print(art.logo)

bid_list = {}
other_bidders = True
while other_bidders:
    # Ask for name, bid
    print("Welcome to the Secret Auction Program.")
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))
    # Add bid to list using name as key and bid as value
    bid_list[name] = bid
    # check for other bidders, if no, end loop
    check_bidders = input("Are there any other bidders? Type yes or no. ").lower()
    if check_bidders == "no":
        highest_bid = 0
        highest_bidder = ""
        for bidder in bid_list:
            if bid_list[bidder] > highest_bid:
                highest_bid = bid_list[bidder]
                highest_bidder = bidder
        print(f"The highest bid was ${highest_bid} from {highest_bidder}. Congratulations {highest_bidder}!")
        print(bid_list)
        print("Goodbye.")
        other_bidders = False
    # if more bidders, clear screen and return to start
    else:
        clear()
        
    