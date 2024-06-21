# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    if len(values) < 1:
        return None
    aggregate = 0
    for num in values:
        aggregate += num
    return aggregate / len(values)


values1 = [5, -1, 10, 7, 2]
values2 = [9, 13, 27, 4]


print(calculate_average(values1))
print(calculate_average(values2))
