# Write a function that meets these requirements.
#
# Name:       biggest_gap
# Parameters: a list of numbers that has at least
#             two numbers in it
# Returns:    the largest gap between any two
#             consecutive numbers in the list
#             (this will always be a positive number)
#
# Examples:
#     * input:  [1, 3, 5, 7]
#       result: 2 because they all have the same gap
#     * input:  [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
#     * input:  [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
#
# You may want to look at the built-in "abs" function

def biggest_gap(num_list):
    if len(num_list) < 2:
        raise ValueError
    # create largest number flag
    largest = 0
    # loop through list and calculate absolute value of gap
    for i in range(1, len(num_list)):
        gap = abs(num_list[i] - num_list[i - 1])
        # update largest if gap is larger
        if gap > largest:
            largest = gap
    return largest


# Test Code
num_list = [1, 3, 5, 7]
print(biggest_gap(num_list))

num_list = [1, 11, 9, 20, 0]
print(biggest_gap(num_list))

num_list = [1, 3, 100, 103, 106]
print(biggest_gap(num_list))
