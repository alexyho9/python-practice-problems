# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_squares(values):
    # initiate total to zero
    total = 0
    # return None if empty list
    if len(values) == 0:
        return None
    # loop through values
    for v in values:
        # square each value and add to total
        total += v ** 2
    # return final total
    return total


list1 = [-5, -2, 0, 3, 9]
list2 = [1, 2]
list3 = []
print(sum_of_squares(list1))
print(sum_of_squares(list2))
print(sum_of_squares(list3))
