#The treasure box was obtained from 'https://ascii.co.uk/art'
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
first_choice = input("Type \"left\" or \"right\".\n ").lower()


if first_choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")

    second_choice = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n ').lower()
    if second_choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")

        third_choice = input("One red, one yellow and one blue. Which colour do you choose?\n ").lower()
        if third_choice == "yellow":
            print("You found the treasure! You Win!")
        elif third_choice == "blue":
            print("You enter a room of beasts. Game Over!")
        elif third_choice == "red":
            print("It's a room full of fire. Game Over!")
        else:
            print("Wrong input. Please try again.")

    elif second_choice == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Wrong input. Please try again.")

elif first_choice == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Wrong input. Please try again.")



#In Python, the backslash (\) is an escape character.
#It tells Python: "The very next character is part of the text, not part of the code."
#Python uses double quotes (" ") to mark the beginning and end of a string. If you wrote:
#input("Type "left" or "right". ")
#Python would think the string ends at the second quote (right before the word left). It would then get confused........
#by the rest of the line and throw a SyntaxError.
#By using \", you are saying: "Don't end the string here; just print a literal double-quote character on the screen."



#You can avoid the backslashes entirely by mixing single and double quotes:
#Use single quotes for the outside:
#input('Type "left" or "right". '), like I did above in 'second_choice '.
#Use double quotes for the outside (and singles inside):
#input("Type 'left' or 'right'. ")



#In an 'input()' function, '.lower()' is used to standardize the user's answer.
#It converts whatever the user types into all lowercase letters, which prevents your if statements from breaking just...
#because someone used a Capital Letter.

