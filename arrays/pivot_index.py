"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.
The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.
If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.
Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.
Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""


def pivot_index(nums):
    for i in range(len(nums)):
        left_sub_list = nums[0:i]
        sum_l = sum(left_sub_list)
        right_sub_list = nums[i+1:]
        sum_r = sum(right_sub_list)

        if sum_l == sum_r:
            return i
    return -1


print(pivot_index([1, 3, 7, 6, 8, 3]))
print(pivot_index([1, 2, 3]))
print(pivot_index([11, 7, 11]))
