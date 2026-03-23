rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Human's turn
print("The most intense 'Rock', 'Paper', 'Scissors' Game")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
if choice == 0:
    print(rock)
    print("Rock")
elif choice == 1:
    print(paper)
    print("Paper")
elif choice == 2:
    print(scissors)
    print("Scissors")
else:
    print("Invalid choice! Choose 0, 1, or 2.")


#Computer's turn
import random

computers_choice = random.randint(0,2)
print(f"AI chose: {computers_choice}")

if computers_choice == 0:
    print(rock)
    print("Rock")
elif computers_choice == 1:
    print(paper)
    print("Paper")
elif computers_choice == 2:
    print(scissors)
    print("Scissors")

#Decision
if choice == computers_choice:
    print("Draw! Play again")
elif (choice == 0 and computers_choice == 1) or (choice == 2 and computers_choice == 0) or (choice == 1 and
                                                                                        computers_choice == 2):
    print("You lose!")
elif (choice == 1 and computers_choice == 0) or (choice == 0 and computers_choice == 2) or (choice == 2 and
                                                                                          computers_choice == 1):
    print("You win!")

#Angela's solution
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")