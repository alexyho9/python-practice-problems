# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

sample = [-5, 14, 9, 2, 23, -1, 25]

def find_second_largest(values):
    # evaluate length of list
    if len(values) < 2:
        return None
    # create variables
    largest = values[0]
    second = values[0]
    # loop through values
    for num in values[1:]:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num
    # return second largest
    return second, largest

print(find_second_largest(sample))
