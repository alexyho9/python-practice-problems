# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    total = 0
    if len(values) == 0:
        return None
    for num in values:
        total += num
    average = total / len(values)
    # print(average)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


print(calculate_grade([92, 75, 88, 71]))
print(calculate_grade([92, 100, 97, 89]))
print(calculate_grade([83, 75, 64, 71]))
print(calculate_grade([52, 75, 83, 61]))
print(calculate_grade([52, 55, 47, 61]))
print(calculate_grade([]))
