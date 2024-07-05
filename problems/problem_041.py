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
    # create result variable
    result = []
    # iterate over list
    for line in csv_lines:
        # separate by comma
        line = line.split(",")
        # create sum variable to hold local sum
        local_sum = 0
        # iterate over items
        for item in line:
            # convert to number and add to local sum
            local_sum += int(item)
        # append local sum to result list
        result.append(local_sum)
    return result


print(add_csv_lines([]))            # []
print(add_csv_lines(["3", "1,9"]))  # [3, 10]
print(add_csv_lines(["8,1,7", "10,10,10", "1,2,3"]))    # [16, 30, 6]
