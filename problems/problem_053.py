# Write a function that meets these requirements.
#
# Name:       username_from_email
# Parameters: a valid email address as a string
# Returns:    the username portion of the email address
#
# The username portion of an email is the substring
# of the email address that appears before the @
#
# Examples
#    * input:   "basia@yahoo.com"
#      returns: "basia"
#    * input:   "basia.farid@yahoo.com"
#      returns: "basia.farid"
#    * input:   "basia_farid+test@yahoo.com"
#      returns: "basia_farid+test"

def username_from_email(email_string):
    arroba = None
    # loop and search for arroba
    for i in range(len(email_string)):
        if email_string[i] == "@":
            # note the index where we find arroba
            arroba = i
    # return a substring up to arroba
    return email_string[:arroba]


# TEST CODE
print(username_from_email("alexyho9@gmail.com"))
print(username_from_email("alexander.ho@fremont.gov"))
print(username_from_email("alexander.ho@tax.hrblock.com"))
