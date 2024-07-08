# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

import math


def halve_the_list(values):
    half_point = math.ceil(len(values)/2)
    return values[0:half_point], values[half_point:]


print(halve_the_list([1, 2, 3, 4]))
print(halve_the_list([1, 2, 3]))
print(halve_the_list([5, 6, 7, 8, 9]))
