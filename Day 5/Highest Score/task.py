import random
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
#Sum function
total_score = sum(student_scores)
print(total_score)
#trying the sum function with for loops
sum = 0
for score in student_scores:
    sum += score

print(sum)

#Max function
Highest_score = max(student_scores)
print(Highest_score)

#trying the max function with for loops
max = 0
for highest in student_scores:
    if highest > max:
        max = highest

print(max)


#Min function
print(min(student_scores))

#trying min function with for loops
min = 0
for lowest in student_scores:
    if lowest < min:
        min = lowest
        print(min)

