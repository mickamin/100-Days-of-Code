print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n $"))
tip_percent = int(input('How much tip would you like to give (%)? 10, 12, or 15?\n'))

if tip_percent not in (10, 12, 15):
    print("The tip should be either 10, 12 or 15%!")
else:
    people = int(input("How many people to split the bill?\n"))
    total_bill = bill * (1 + tip_percent / 100)
    amount_per_person = total_bill / people
    final_amount = round(amount_per_person, 2)
    print(f'Each person should pay ${final_amount}')