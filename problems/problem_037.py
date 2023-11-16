# Complete the pad_left function which takes three parameters
#   * a number
#   * the number of characters in the result
#   * a padding character
# and turns the number into a string of the desired length
# by adding the padding character to the left of it
#
# Examples:
#   * number: 10
#     length: 4
#     pad:    "*"
#     result: "**10"
#   * number: 10
#     length: 5
#     pad:    "0"
#     result: "00010"
#   * number: 1000
#     length: 3
#     pad:    "0"
#     result: "1000"
#   * number: 19
#     length: 5
#     pad:    " "
#     result: "   19"

def pad_left(number, length, pad):
    # initiate variables
    char_number = len(str(number))
    # if char_number length is longer than length, return number
    if char_number >= length:
        return str(number)
    # else add padding to the left of number until it fills length
    else:
        # count difference between length and character length
        pad_count = length - char_number
        # concatenate string of padding and number
        return str(pad_count * str(pad)) + str(number)


print(pad_left(10, 4, "*"))
print(pad_left(10, 5, "0"))
print(pad_left(1000, 3, "0"))
print(pad_left(19, 5, " "))
