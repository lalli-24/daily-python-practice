# Brute Force

nums = [2, 7, 11, 15]
target = 9
for x in range(len(nums)):
    for y in range(x + 1, len(nums)):
        if nums[x] + nums[y] == target:
            print([x, y])
            break


# Using HashMap

nums = [2,7,11,15]
target = 9

d = {}
for x in range(len(nums)):

    c = target - nums[x]

    if c in d:
        print([d[c], x])
        break

    d[nums[x]] = x
