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


def halve_the_list(list1):
    # find the halfway mark and round up
    halfway_index = math.ceil(len(list1) / 2)
    # create first and second lists
    list_a = list1[:halfway_index]
    list_b = list1[halfway_index:]
    # return both results
    return list_a, list_b


# TEST CODE
list1 = [1, 2, 3, 4, 5, 6, 7]
print(halve_the_list(list1))

list1 = [1, 2, 3, 4, 5, 6]
print(halve_the_list(list1))

list1 = [1, 2, 3, 4]
print(halve_the_list(list1))
