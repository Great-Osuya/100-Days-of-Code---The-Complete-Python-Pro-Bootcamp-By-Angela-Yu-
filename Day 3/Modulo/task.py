# Modulo operator is one that gives you the remainder of a divison operation.
print(10 % 3) #this gives '1' as the answer because 3 divides 10, 3 times but remains 1
print(25 % 5) #this will give '0' because there is no remainder

#Even or Odd Number Checker
print("What number do you want to check?")
number = float(input("Number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#Check if a number is divisble by 7
print("What number do you want to check?")
number = float(input("Number: "))

if number % 7 == 0:
    print(f"{number} is a multiple of 7")
else:
    print(f"{number} is not a multiple of 7")