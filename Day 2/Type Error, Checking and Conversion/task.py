print(len("12345"))

#Data Type function: type()
print(type("abc"))
print(type(12345))
print(type(1234.5))
print(type(True))

#Type Conversion/ Type Casting:
int() # converts to integer
float() # converts to float (decimal)
str() # converts to string
bool() # converts to bool

print(int("123") + int("456")) # See that it still sums it up even though there are double quotes

# Question: Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))
# The reason there was error is because you can not concatenate Integers (The number of letters in name is an integer).
print("Number of letters in your name: " + str(len(input("Enter your name")))) # So you convert it into a string which can be concatenated

# The above is simplified below:
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_name))