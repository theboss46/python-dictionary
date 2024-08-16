nums = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for num in nums:
    if num not in uniques:
        uniques.append(num)
print(uniques)
