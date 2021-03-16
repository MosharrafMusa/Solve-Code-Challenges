# Consider an arithmetic expression of the form a#b=c.
# Check whether it is possible to replace # with one
#  of the four signs: +, -, * or / to obtain a correct expression.

# Example

# For a = 2, b = 3, and c = 5, the output should be
# arithmeticExpression(a, b, c) = true.

# We can replace # with a + to obtain 2 + 3 = 5, so the answer
#  is true.

# For a = 8, b = 2, and c = 4, the output should be
# arithmeticExpression(a, b, c) = true.

# We can replace # with a / to obtain 8 / 2 = 4, so the answer
#  is true.
def arithmeticExpression(a, b, c):
    if a + b == c:
        return True
    elif a - b == c:
        return True
    elif a * b == c:
        return True
    elif a / b == c:
        return True
    return False


print(arithmeticExpression(8, 2, 4))
