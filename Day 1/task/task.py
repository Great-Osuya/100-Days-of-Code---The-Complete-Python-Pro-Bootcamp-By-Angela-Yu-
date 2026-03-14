# you can name your variable anything just make ure it is readable and as specific as possible.
# avoid using functions as the names of your variable "print", "input", etc.
name = input("What is your name")
print(name)

x = "John"
print(x)

x = "Mark"
print(x)
# note that the functon "len()," is to determine number of characters.
print(len(name))

# Pause 1
print(len(input("What is your name?")))
# Pause 2
username= input("Username")
length= len(username)
print(length)

# below is how you switch variables
name = input("What is your name")
gender = input("gender")
name, gender = gender, name
print(name, gender)
print(gender, name)
# or you could switch like this. I am keeping the above name and gender variables the same below
name = input("What is your name")
gender = input("gender")
temp= name
name= gender
gender= temp
print(name, gender)
print(gender, name)
print(temp)
# you can use anything as the temporary variable. Most people use "temp" but any order random thing is fine