# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

numbers = [43, 19, 4, 25]
numbers2 = []
numbers3 = [1, 2, 3, 4, 5]

def calculate_sum(values):
    total = 0
    # return none if empty
    if len(values) == 0:
        return None
    # add up all the numbers in list
    else:
        for num in values:
            total += num
        return total

print(calculate_sum(numbers))
print(calculate_sum(numbers2))
print(calculate_sum(numbers3))
