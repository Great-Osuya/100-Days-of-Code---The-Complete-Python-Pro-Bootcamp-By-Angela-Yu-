

for number in range(1, 10): #"does not include '10'"
    print(number)

for number in range(0, 11, 2): #"the '2' shows the gap it will move by. so 0,2,4,6,8,10"
    print(number)

#THE Gauss challenge
final = 0
for number in range(1, 101):
    final += number

print(final)