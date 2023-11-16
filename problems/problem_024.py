# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    # returns the average of a list of numbers.
    length = len(values)
    total = 0
    # if length is zero, return none
    if len(values) == 0:
        return None
    else:
        # add up items in values
        for num in values:
            total += num
    # calculate average
        return total / length

print(calculate_average([4, 9, -3, 24, 15]))
print(calculate_average([1, 2, 3, 4, 5]))
