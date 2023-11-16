# Write a function that meets these requirements.
#
# Name:       num_concat
# Parameters: two numerical parameters
# Returns:    the concatenated string conversions
#             of the numerical parameters
#
# Examples:
#     input:
#       parameter 1: 3
#       parameter 2: 10
#     returns: "310"
#     input:
#       parameter 1: 9238
#       parameter 2: 0
#     returns: "92380"

def num_concat(x, y):
    # convert arguments to strings
    # add strings together
    return str(x) + str(y)


# Test Code
print(num_concat(3, 10))
print(num_concat(10, 3))
print(num_concat(9238, 0))
print(num_concat(0, 14))
