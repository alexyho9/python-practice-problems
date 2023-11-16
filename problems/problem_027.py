# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#
samples = [3, 26, -9, 17]

def max_in_list(values):
    # make starting variable
    largest = 0
    # loop through items
    for item in values:
        if item > largest:
            # compare item to largest
            largest = item
    # return largest
    return largest


print(max_in_list(samples))
