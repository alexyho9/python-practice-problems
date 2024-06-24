# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if len(values) == 0:
        return None
    highest = values[0]
    for num in values:
        if num > highest:
            highest = num
    return highest


print(max_in_list([-4, -10, 13, 7]))
print(max_in_list([]))
print(max_in_list([72, -10, 13, 7]))
print(max_in_list([-54, -10, -32, -27]))
