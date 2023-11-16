# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def shift_letters(string1):
    # Create list of lower and upper alphabet for index ref
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # loop through string1 and get index. increment index and return.
    new_string = ""
    for letter in string1:
        if letter.islower():
            i = (lower.index(letter) + 1) % 26
            new_string += lower[i]
        elif letter.isupper():
            i = (upper.index(letter) + 1) % 26
            new_string += upper[i]
    return new_string


# Test Code
string1 = "import"
print(shift_letters(string1))

string1 = "ABBA"
print(shift_letters(string1))

string1 = "Kala"
print(shift_letters(string1))

string1 = "zap"
print(shift_letters(string1))
