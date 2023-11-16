# Complete the is_divisible_by_5 function to return the
# word "buzz" if the value in the number parameter is
# divisible by 5. Otherwise, just return the number.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def is_divisible_by_5(number):
    # test if divisible by 5
    if number % 5 == 0:
    # return buzz
        return "buzz"
    # else return number
    else:
        return number


print(is_divisible_by_5(15))
print(is_divisible_by_5(-100))
print(is_divisible_by_5(34))
print(is_divisible_by_5(17))
