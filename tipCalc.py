

print("Welcome to the tip calculator.")

total = float(input("What was the total bill? "))

tip = int(input("What percentage tip would you like to give? "))

num_people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100 
tip_amount = total * tip_as_percent
new_total = total + tip_amount
print(new_total)

share = round(new_total / num_people,2)

print(f"Each person should pay: {share}")