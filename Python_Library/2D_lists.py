# 2d lists are list where each item in the list countains a list

matrix = [
    [1, 2, 3],
    [4, 5, 6],  # dont forget the comas after the lists
    [7, 8, 9]
]
# the first index number picks the lines of the list. The second index number picks the item from the list
print(matrix[1][2])

# You can also change item in them
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2[2][1] = 20
print(matrix2[2][1])

# this how you would use nested loops to itterate over all the items in the matrix
matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
