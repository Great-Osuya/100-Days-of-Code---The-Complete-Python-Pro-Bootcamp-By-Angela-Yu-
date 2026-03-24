fruits = ["Apple", "Peach", "Pear"]

for item in fruits: #<item> is basically just an word you come up with. if I used "greens" it will still work
    print(item)
    print(item + "pie")

print("\ntrial 2")
for greens in fruits:
    print(greens)

#the way the "for loop" works is that this:
#the compiler goes down the code, executes that, then repeats that until it finishes
#this is why it first prints <Apple>, then <Applepie> before it even moves to any other item in the list.
#it must exhaust all the functions tied to one item completely before it can move to the next, and repeat that..........
#until the very last item
#indentation is also very importan here just like in the <if, elif else> function
print("\ntrial 3")
for item in fruits:
    print(item)
    print(item + "pie")
print(fruits)
#observe that the two are not the same thing
print("\ntrial 4")
for item in fruits:
    print(item)
    print(item + "pie")
    print(fruits)

