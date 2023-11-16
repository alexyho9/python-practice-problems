# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

sample = "racecar"
sample2 = "onomatopoeia"

def remove_duplicate_letters(s):
    # create variable
    result = ""
    # loop through letters
    for letter in s:
        # if the letter is new, add to final result
        if letter not in result:
            result += letter
        # if the letter is already there, don't add to final result
    # return final result
    return result

print(remove_duplicate_letters(sample))
print(remove_duplicate_letters(sample2))
