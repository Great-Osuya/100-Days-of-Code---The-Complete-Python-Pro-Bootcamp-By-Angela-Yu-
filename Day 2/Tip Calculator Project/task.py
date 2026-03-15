# My Solution
print("Welcome to GREAT's tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
tip /= 100
tip += 1
people = int(input("How many people to split the bill? "))
pay = float(bill / people * tip)
print(round(pay, 2))
print(f"Each person should pay: ${float(round(pay, 2))}")

print("\n")

# ANGELA'S SOLUTION
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")
