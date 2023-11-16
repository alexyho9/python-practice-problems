# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

attendees = ['a', 'b', 'c']
members = range(5)

def has_quorum(attendees_list, members_list):
    # length of attendees
    count_attendees = len(attendees_list)
    # length of members
    count_members = len(members_list)
    # evaluate condition
    return count_attendees >= count_members // 2


print(has_quorum(attendees, members))

members = range(10)
print(has_quorum(attendees, members))
