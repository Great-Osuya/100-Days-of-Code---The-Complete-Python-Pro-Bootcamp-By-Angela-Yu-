import random



#Mersene Twister is the Pseudorandom Number Generators that python uses
#Read this https://en.wikipedia.org/wiki/Mersenne_Twister
#Watch this https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs
#For the various functions for random numbers, read this document https://docs.python.org/3/library/random.html ...
#The random module makes it easy to use Pseudorandom number generators with learning the complex math

print(random.randint(1,10)) #a <= N <= b (where a, b and N are always integers)
#This generates a random integer between and inclusive of 1 and 10

print(random.random()) # 0.0 <= N < 1.0
#random.random() function generates a number between 0 and 1, but always less than 1
print(random.random() * 10 ) #multiplying by 10 increases the range to be "0.0 <= N < 10"

print(random.uniform(0.1,10.5))  #a <= N <= b (where a, b and N are floating )[can also be integers, but it will......
# generate floats]

import My_Module
print(My_Module.Goldfish)
# So basically, this is how it works, you create a file, then you import it. Type in the name of the file, then a dot...
#followed by the name of a component of the file (a content within the file). e.g.
#Assuming the name of the file is <filename> and the content is <content/component>
#Next type; <Import filename>
#then to select the specific component you want to highlight or make use of.
# i.e. <filename.content/component>

#my solution
Heads_or_tails = random.randint(0,10)
if Heads_or_tails % 2 == 0:
    print("Heads") #so if the number is even, it should print heads
else:
    print("Tails") #if it is odd, it should print tails

#Angela's solution
random_head_or_tails = random.randint(0,1)
if random_head_or_tails == 0:
    print("Heads")
else:
    print("Tails")