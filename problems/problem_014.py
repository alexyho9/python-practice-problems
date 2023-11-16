# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

ingredients = ['flour', 'eggs', 'oil']
ingredients2 = ['flour', 'rice', 'oil']

def can_make_pasta(ingredients):
    # sufficient?
    sufficient = False
    # evaluate what's in the list
    if 'flour' in ingredients and 'eggs' in ingredients and 'oil' in ingredients:
        return True
    # determine if we are sufficient or lacking
    else:
        return False

print(can_make_pasta(ingredients))
print(can_make_pasta(ingredients2))
