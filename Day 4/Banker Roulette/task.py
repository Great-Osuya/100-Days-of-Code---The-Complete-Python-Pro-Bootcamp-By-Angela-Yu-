friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
#trial 1
choice = random.randint(1,5)
if choice == 1:
    print("Alice")
elif choice == 2:
    print("Bob")
elif choice == 3:
    print("Charlie")
elif choice == 4:
    print("David")
elif choice == 5:
    print("Emanuel")


#trial 2
loser = random.choice(friends) #<random.choice> is used to select an item from a list randomly
print(loser)
#or
print(random.choice(friends))

#trial 3
random_index = random.randint(0,4)
print(friends[random_index])
#why this one works us because each item in the list has a number from 0 to 4...
#taking into account the fact that <random-index> becomesa variable that stores the integer randomly generated,...
#then using the standard code <list[item_number_in_the_list]>...
#so waht that gives us is <friends[random_index]>
