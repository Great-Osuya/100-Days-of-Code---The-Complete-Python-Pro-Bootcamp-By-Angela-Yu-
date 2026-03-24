fruits = ["Apple", "Peach", "Pear"]

for item in fruits:
    print(item)
    print(item + "pie")

#the way the "for loop" works is that this:
#the compiler goes down the code, executes that, then repeats that until it finishes
#this is why it first prints <Apple>, then <Applepie> before it even moves to any other item in the list.
#it must exhaust all the functions tied to one item completely before it can move to the next, and repeat that..........
#until the very last item