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

# the 'elif' is weird. I am not sure if I see the relevance of it.
# 'Elif' is 'else if'. So it adds another condition that goes inbetween the 'if' condition and the 'else' condition.
# this third condition is more like a middle ground that once it is proven wrong, it goes straight to the 'else' condition
# basically: 'If' condition -> 'Elif' condition -> 'Else' condition
# so when structuring the 'Elif" condition always think of a condition takes into consideration everything that...
# 'If' could not, so that 'else' can cover what remains