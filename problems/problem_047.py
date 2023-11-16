# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    # create variables for conditions
    lowercase_check = False
    uppercase_check = False
    digit_check = False
    special_check = False
    length_check = False
    # check each condition with if-statements
    for char in password:
        if char.isalpha() and char.islower():
            lowercase_check = True
        if char.isalpha() and char.isupper():
            uppercase_check = True
        if char.isdigit():
            digit_check = True
        if char in "!@#$%^&*-+?/[]":
            special_check = True
    if 6 <= len(password) <= 12:
        length_check = True

    # return if all true
    return (
        lowercase_check and uppercase_check and digit_check
        and special_check and length_check
    )


sample1 = "NewYork#1"
print(check_password(sample1))

sample1 = "3Embarcadero!"
print(check_password(sample1))

sample1 = "India"
print(check_password(sample1))

sample1 = "32704BelAireSt"
print(check_password(sample1))

sample1 = "3rd&Market"
print(check_password(sample1))
