# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4

def sum_fraction_sequence(number):
    # create total placeholder
    total = 0
    chain = []
    # loop through range to number
    for i in range(1, number + 1):
        # in each iteration, retrieve index and create fraction w denom of i+1
        fraction_value = i / (i+1)
        # also create string representation of sequence
        fraction_string = str(i) + "/" + str(i+1)
        # append new fraction to total
        total += fraction_value
        chain.append(fraction_string)
    chain_string = " + ".join(chain)
    return total, chain_string


# Test Code
print(sum_fraction_sequence(1))
print(sum_fraction_sequence(2))
print(sum_fraction_sequence(3))
