# Complete the is_divisible_by_3 function to return the
# word "fizz" if the value in the number parameter is
# divisible by 3. Otherwise, just return the number.
#
# You can use the test number % 3 == 0 to test if a
# number is divisible by 3.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def is_divisible_by_3(number):
    # test if divisible by 3
    if number % 3 == 0:
    # return fizz
        return "fizz"
    # if not divisible by 3, return the number
    else:
        return number

print(is_divisible_by_3(18))
print(is_divisible_by_3(9))
print(is_divisible_by_3(22))
print(is_divisible_by_3(4))
