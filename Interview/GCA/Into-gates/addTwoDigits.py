# 1. You are given a two-digit integer n. Return the sum of its digits.
# For n = 29, the output should be addTwoDigits(n) = 11.
# For n = 48, the output should be addTwoDigits(n) = 12.

# How to sum the digits of a number in Python
# The sum of the digits of a number means adding up each
# of the digits and returning the sum. For instance, the
# sum of the digits of 123 is 6.

# ITERATE OVER EACH DIGIT
# Use str() to convert a number to a string. Create a for-loop to
# iterate over each digit in the string. Use int() to convert
# the string digit to an integer. Add this digit to the sum of
# the digits in each iteration.

number = 123

sum_of_digits = 0
for digit in str(number):
    # turn to string to iterate through

    sum_of_digits += int(digit)

print(sum_of_digits)
