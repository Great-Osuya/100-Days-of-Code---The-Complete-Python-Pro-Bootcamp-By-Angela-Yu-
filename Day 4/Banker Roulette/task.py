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
