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
    if denominator == 0:
        return math.inf
    return numerator / denominator


print(safe_divide(9, 3))    # 3.0
print(safe_divide(9, 2))    # 4.5
print(safe_divide(9, 0))    # inf
