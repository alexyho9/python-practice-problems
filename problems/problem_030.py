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

def find_second_largest(values):
    if len(values) < 2:
        return None
    largest = values[0]
    second = values[1]
    for num in values:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    print(largest, second)
    return second


print(find_second_largest([-4, -6, -3, -7]))
print(find_second_largest([-5, 7, 2, 1]))
print(find_second_largest([9, -1, 0]))
print(find_second_largest([-1, 9, 0]))
