def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return (lookup[target - num], i)
        lookup[num] = i


print(twoSum([2, 1, 1, 3], 4))
