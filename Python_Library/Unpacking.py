# we use unpacking to shorten the amount of code we need to write out.
# to show this i will show the long way(no unpacking) and the short way(with unpacking)


coordinates = (1, 2, 3)  # can be list or tuple

# This first method does not use unpacking
print('FIRST METHOD: ', coordinates[0] + coordinates[1] + coordinates[2])

# This next method is a more visual representation of how unpacking works.
# unpacking turns each elemnt of the list or tuple into into there own variable sort of like this
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print('VISUAL REPRESENTATION(SECONT METHOD): ', x + y + z)

# This method used unpacking to create each of the variables.
x1, y1, z2 = coordinates  # This is the same as above. But compact.
print('THIRD METHOD(USING UNPACKING): ', x1 + y1 + z2)
