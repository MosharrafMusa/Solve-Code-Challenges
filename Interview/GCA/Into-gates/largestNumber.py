# 2.Given an integer n, return the largest number that contains exactly n digits.
# For n = 2, the output should be
# largestNumber(n) = 99.
def largestNumber(n):
    x = pow(10, n)-1
    return x


print(largestNumber(4))
