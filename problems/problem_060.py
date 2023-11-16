# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
#     * input:   [1, 2, 3, 4]
#       returns: [1, 3]
#     * input:   [2, 4, 6, 8]
#       returns: []
#     * input:   [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]

def only_odds(lst):
    # loop through original lst and take odds
    return [x for x in lst if x % 2 != 0]


# Test Code
sample_set = [1, 2, 3, 4]
print(only_odds(sample_set))

sample_set = [2, 4, 6, 8]
print(only_odds(sample_set))

sample_set = [1, 3, 5, 7]
print(only_odds(sample_set))
