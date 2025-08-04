nums = [10, 13, 20, 33, 40, 17, 25, 8]
even_nums = []
odd_nums = []
multiples_of_5 = []

for x in nums:
    if x % 2 == 0:
        even_nums.append(x)
    else:
        odd_nums.append(x)
    if x % 5 == 0:
         multiples_of_5.append(x)
print(even_nums)
print(odd_nums)
print(multiples_of_5)
