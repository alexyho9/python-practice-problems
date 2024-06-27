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

def remove_duplicate_letters(s):
    result = ""
    for letter in s:
        if letter not in result:
            result += letter
    return result


print(remove_duplicate_letters("abc"))
print(remove_duplicate_letters("abcabc"))
print(remove_duplicate_letters("abccba"))
print(remove_duplicate_letters("abccbad"))
