#a list is a way of storing a group of connected data in 1 variable
#This is a list: <fruits[item1, item2, item3]>
#the items have an order determined by the order in which they are arranged in the list

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0]) #You always use a square bracket <[]> to indicate the item you need to access
# #note that we start counting from <0>, think of this as an offset.
#The start has no offset, so zero, but the next is offset by 1 (1 is added) and for the next 2 and so on and so forth.
print(states_of_america[1])

print(states_of_america[-1]) #this dignifies the last item on the least
print(states_of_america[-2])

#To alter am item in the least
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

#To add to the end of the list
states_of_america.append("Greatland")
print(states_of_america[-1])

#TO extend the list and add more items to the list
states_of_america.extend(["Angelaland", "Metraton"])
print(states_of_america[-3], states_of_america[-2], states_of_america[-1])