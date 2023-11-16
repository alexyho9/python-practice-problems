# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

import random


def specific_random():
    # create a list of eligible numbers (divisible by 5 and 7) using loop
    eligible_numbers = [num for num in range(10, 501) if num % 5 == 0 and num % 7 == 0]
    # choose a random eligible number
    return random.choice(eligible_numbers)


# Test Code
print(specific_random())
print(specific_random())
print(specific_random())
