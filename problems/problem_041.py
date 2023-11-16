# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.

def add_csv_lines(csv_lines):
    # create new list
    new_list = []
    # loop over each original list item
    for i in csv_lines:
        # create placeholder total
        total = 0
        # split string by comma separator
        for j in i.split(","):
            # convert strings to numbers
            total += int(j)
        # add numbers in each list
        new_list.append(total)
    # return new list
    return new_list


# Test code
list_a = []
list_b = ["3", "1,9"]
list_c = ["8,1,7", "10,10,10", "1,2,3"]

print(add_csv_lines(list_a))
print(add_csv_lines(list_b))
print(add_csv_lines(list_c))
