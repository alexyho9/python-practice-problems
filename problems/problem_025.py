# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    if len(values) == 0:
        return None
    result = 0
    for num in values:
        result += num
    return result


print(calculate_sum([4, 95, -12, 37]))
print(calculate_sum([1, 2, 3, 4]))
print(calculate_sum([]))