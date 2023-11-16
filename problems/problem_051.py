# Write a function that meets these requirements.
#
# Name:       safe_divide
# Parameters: two values, a numerator and a denominator
# Returns:    if the denominator is zero, then returns math.inf.
#             otherwise, returns numerator / denominator
#
# Don't for get to import math!

import math


def safe_divide(numerator, denominator):
    # Check if denominator is zero
    if denominator == 0:
        return math.inf
    # go on and do the division
    return numerator / denominator


# TEST CODE
print(safe_divide(4, 0))
print(safe_divide(4, 8))
print(safe_divide(2, 10))
print(safe_divide(24, 8))
