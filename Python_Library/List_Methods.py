# Here you will learn the different operations you can perform on a list

# you can add data to a list by using the append operator
nums = [5, 2, 1, 7, 4]
nums.append(20)
print(nums)

# Append does not work to add data to the start of the list.
# if you want to put the data in the start of the list or anywhere else you should use the insert operator
nums2 = [5, 2, 1, 7, 4]
# the first number is the index and the second number is the number you want to insert
nums2.insert(0, 10)
print(nums2)  # Remember that it only adds it in not replaces that value

# You can also remove numbers from the list by using the remove operator
nums3 = [5, 2, 1, 7, 4]
nums3.remove(5)  # Removes all the number that have the same value
print(nums3)

# You can also remove all the numbers from the list by using the clear operator
nums4 = [5, 2, 1, 7, 4]
nums4.clear()
print(nums4)

# To remove the last item from a list by using the pop operator
nums5 = [5, 2, 1, 7, 4]
nums5.pop()
print(nums5)

# If you want to find an item from a list you use the index operator
nums6 = [5, 2, 1, 7, 4]
print(nums6.index(5))

# there is another way to find an item from a list that will give a boolean value. for this example you need to use the in operator
nums7 = [5, 2, 1, 7, 4]
print(5 in nums7)

# To fing the amount of time an item occurs in the list you use the count operator
nums8 = [5, 2, 1, 7, 4, 5]  # here i added a 5 to the end
print(nums8.count(5))

# also you can sort the items in a list in accending order by using the sort operator
nums9 = [5, 2, 1, 7, 4]
# When this prints it will show 'none'. None is printed because it represents the absense of a value
print(nums9.sort())
# There is absense of a value because the operator is only sorting the list and does not have any return values.
# if we actually want to see this sorted list, we would do this
nums10 = [5, 2, 1, 7, 4]
nums10.sort()  # this always sorts the list in ascending order
print(nums10)

# if you wanted to make the list be in descending order then you would have to use the reverse operator.
nums11 = [5, 2, 1, 7, 4]
nums11.sort()
nums11.reverse()
print(nums11)

# you can also use the copy operator to copy the list
nums12 = [5, 2, 1, 7, 4]
nums12copy = nums12.copy()
# i have printed both to show that they are both stored seperately.
print(nums12, '\n', nums12copy)
# this mean you can add values to own and it will not effect the other.

# CHALLENGE
# Write a program that removes the duplicates in a list of numbers
# Find the answers in remove_duplicated_items.py
