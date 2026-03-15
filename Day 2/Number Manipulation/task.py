bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi)) # This floors the number to the lowest whole number

print(round(bmi)) # This rounds it to the nearest whole number without decimals

print(round(bmi, 2)) # This rounds it to the required decimal place specified. 2 in this case is 2 decimal places

# Assignment Operators: Allows you to make mathematical changes to the original value of a variable without having to refer back to the old value
score = 100  # In this case, score is the default amount of maximum points allotted initially
score += 5  # A student gains 5 points extra (100 + 5 = 105)
score -= 10  # The student losses 10 extra points (105- 10 = 95)
score *= 4 # The student gains bonuses worth 4 times the current score (95 * 4 = 380)
score /= 5 # The student losses 1/5th his current score (380 / 5 = 76)
print("Final Score = " + str(score))

# f-Strings: Makes it possible to mix strings and other different data types
score = 0
height= 1.8
is_winning = True
print(f"Your score is = {score}. Your height is = {height}m, Your winning is {is_winning}")
# the presence of 'f' before the double quote in addition to variable being placed in the squiggly brackets '{}', makes it possible to mix string and other data types