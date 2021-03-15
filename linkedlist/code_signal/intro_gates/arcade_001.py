# You are given a two-digit integer n. Return the sum of its digits.

# Example

# For n = 29, the output should be
# addTwoDigits(n) = 11.

def addTwoDigits(n):
    sum1 = 0
    for i in str(n):
        sum1 += int(i)
    return sum1


print(addTwoDigits(29))
