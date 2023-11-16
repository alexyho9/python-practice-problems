# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    # create empty list to initiate
    need = []
    # not sunny and workday
    if not is_sunny and is_workday:
        need.append("umbrella")
    # workday
    if is_workday:
        need.append("laptop")
    # not workday
    else:
        need.append("surfboard")
    return need


print(gear_for_day(True, True))
print(gear_for_day(False, False))
print(gear_for_day(True, False))
print(gear_for_day(False, True))
