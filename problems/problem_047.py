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
    lower = False
    upper = False
    digit = False
    special = False
    length = False
    if len(password) >= 6 and len(password) <= 12:
        length = True
    else:
        return False
    for char in password:
        if char.isalpha():
            if char.isupper():
                upper = True
            elif char.islower():
                lower = True
        elif char.isdigit():
            digit = True
    if password.count("$") > 0 or password.count("!") > 0 or password.count("@") > 0:
        special = True
    return lower and upper and digit and special and length


print(check_password("apple"))
print(check_password("pokemon123"))
print(check_password("$100Dollars"))
