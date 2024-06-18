# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):
    flour_test = False
    egg_test = False
    oil_test = False
    for item in ingredients:
        if item == "flour":
            flour_test = True
        elif item == "eggs" or item == "egg":
            egg_test = True
        elif item == "oil":
            oil_test = True
    # print(flour_test, egg_test, oil_test)
    if flour_test and egg_test and oil_test:
        return True
    return False


list1 = ["apples", "figs", "pecans"]
list2 = ["beetles", "eggs", "blues"]
list3 = ["flour", "eggs", "oil"]
list4 = ["eggs", "oil", "flour"]

print(can_make_pasta(list1))
print(can_make_pasta(list2))
print(can_make_pasta(list3))
print(can_make_pasta(list4))
