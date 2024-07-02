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
    result = ""
    num_string = str(number)

    for char in num_string[::-1]:
        result = char + result
        length -= 1

    while length > 0:
        result = pad + result
        length -= 1

    return result


print(pad_left(10, 4, "*"))     # "**10"
print(pad_left(10, 5, "0"))     # "00010"
print(pad_left(1000, 3, "0"))   # "1000"
print(pad_left(19, 5, " "))     # "   19"
