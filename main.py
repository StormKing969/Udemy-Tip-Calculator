print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage = float(input("What percentage tip would you like to give? "))

bill = total_bill / people
tip = round(bill * (percentage / 100), 2)
total_price = round(bill + tip, 2)

# Making use of the f-String
print(f"Each person give a tip of: ${tip} i.e pay ${total_price}")
