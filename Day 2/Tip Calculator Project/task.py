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

