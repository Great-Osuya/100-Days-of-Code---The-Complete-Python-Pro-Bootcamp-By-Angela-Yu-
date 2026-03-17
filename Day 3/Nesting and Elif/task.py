print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster.")

    age = int(input("How old are you? "))

    if age >= 18:
        print("Please pay $12.")
    if 12 <= age < 18:
        print("please pay $7.")
    if age < 12:
        print("Please pay $5.")
else:
    print("Sorry you have to grow taller before you can ride.")

#Trying the above with "Elif"
height = float(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster.")

    age = int(input("How old are you? "))

    if age < 12:
        print("Please pay $5.")
    elif age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# The main difference between 'if' and 'elif' statement is the fact that every 'if' statement is independent...
# of the previous 'if' statement even if they are in the same code block.
# 'elif' on the other hand is directly connected to the previous 'if' statement.
# Each 'if' statements is seen as its own independent question
# Each 'elif' statement is seen as a part of the whole decision.

#Example

size = 20
if size > 10:
    print("You are size 10.")
if size > 15:
    print("You are size 15.")

#observe that all the 'if' statements were run. 'If' statements are all independent

colour = 20
if colour > 30:
    print("You are colour 30.")
elif colour > 10:
    print("You are colour 10.")
elif colour > 15:
    print("You are colour 15.")

#observe that only the immediate 'elif' that matched the criteria was run. 'elif' statements are all connected to the...
#final big decision. If the 'if' statement had been true, only the 'if' statement will have run, because it was already...
#true, no need to move forward and check any other statement.

#Stacking 'if' (Independent Checks)
#  ~Result: Multiple blocks of code run
#  ~Usage: When you want to check for multiple independent conditions
#  ~Logic: "Check this, THEN check this... (till the last 'if' statement)"
#  ~Efficiency: Slower (Checks every condition)

#Using 'elif' (The 'Either/or' Chain)
#  ~Result: Only one block of code will ever run
#  ~Usage: When conditions are mutually exclusive (if one is true, the other do not matter)
#  ~Logic: "Check this; if not true, try this... (it stops immediately it finds the first true condition)"
#  ~Efficiency: Faster (Stops once it finds a match)