# this is a closer look at lists

name = ['John', 'Lucas', 'Mehtab', 'Tyler', 'Mahim']
print(name)  # when you print a list it will just print everything

name2 = ['John', 'Lucas', 'Mehtab', 'Tyler', 'Mahim']
# we can use an index here to choose a specific name in the list. Remember that it always starts at 0.
print(name2[2])

name3 = ['John', 'Lucas', 'Mehtab', 'Tyler', 'Mahim']
# we can also use a negative index to get the name from the end of the list
print(name3[-1])

name4 = ['John', 'Lucas', 'Mehtab', 'Tyler', 'Mahim']
# we can also use a colon to get a range of items from a list.
# You can specify an end point or you can leave it blank and it will get all the items after you specified poiny
# when using two index numbers the second number will not include the item with that index number.
print(name4[1:4])

# when u index it does not change what the list is saved as in the variable. It simply returns a new list.

# you can modify the list if you want to.
# This is how to do it
name5 = ['John', 'Lucas', 'Mehtab', 'Tyler', 'Mahim']
name5[1] = 'Luca'  # this changes the item with index 1(second item) to luca
print(name5)

# CHALLENGE
# write a program that will find the biggest number in a list of items
# go to find_big_number.py to see the solution
