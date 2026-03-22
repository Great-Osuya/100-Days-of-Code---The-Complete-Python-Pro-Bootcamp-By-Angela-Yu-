states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
#<print(len(states_of_america)) shows you the number of items in the list>

#<off_by_one_error> occurs when the list counting starts from <1> instead of <0>...
#when this occurs, you just simply need to minus 1 e.g.
no_of_states = len(states_of_america)
print(states_of_america[no_of_states]) # because the variable <no_of_states> will be <50>, there will be an error =>
# "IndexError: list index out of range". TO solve this, just minus 1
print(states_of_america[no_of_states - 1]) #This will give us Hawaii which is the 50th state on the list
# (but 49th if we start counting from zero)

#Nested lists or 2D list
#say we have 2 lists fruits and vegetables, and we want to put them in one list:
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
greens = [fruits, veg]
print(greens)

