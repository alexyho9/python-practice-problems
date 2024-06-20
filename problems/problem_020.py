# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    return len(attendees_list) / len(members_list) >= 0.5


members = ["Nerea", "Taylor", "Joseph", "Bean"]
attendees1 = ["Yohan", "Bean", "Nerea", "Shirley"]
attendees2 = ["Jake"]
attendees3 = ["Allison", "Emily"]


print(has_quorum(attendees1, members))
print(has_quorum(attendees2, members))
print(has_quorum(attendees3, members))
