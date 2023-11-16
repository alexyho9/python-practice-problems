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

scores_a = [78, 90, 99, 98, 95]
scores_b = [90, 70, 87, 85, 91]
scores_c = [90, 70, 67, 72, 73]
scores_f = [51, 43, 80, 71, 30]

def calculate_grade(values):
    total = 0
    length = len(values)
    # add scores
    for i in values:
        total += i
    # get average
    average = total / length
    # evaluate letter grade
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

print(calculate_grade(scores_a))
print(calculate_grade(scores_b))
print(calculate_grade(scores_c))
print(calculate_grade(scores_f))
