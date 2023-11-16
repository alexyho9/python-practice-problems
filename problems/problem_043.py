# Complete the find_indexes function which accepts two
# parameters, a list and a search term. It returns a new
# list that contains the indexes of the search term in
# the search list.
#
# Remember that indexes in Python are zero-based. That
# means the first element in the list is index 0.
#
# Examples:
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  4
#     result:       [3]
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  6
#     result:       []
#   * search_list:  [1, 2, 1, 2, 1]
#     search_term:  1
#     result:       [0, 2, 4]
#
# Look up the enumerate function to help you with this problem.

def find_indexes(search_list, search_term):
    # create empty new list
    new_list = []
    # loop through original list using index-range-len
    for index in range(len(search_list)):
        # if item in original list matches search term, add index to new list
        if search_list[index] == search_term:
            new_list.append(index)
    # return new list
    return new_list


# Test Code

list1 = [1, 2, 3, 4, 5]
term = 4
print(find_indexes(list1, term))

list1 = [1, 2, 3, 4, 5]
term = 6
print(find_indexes(list1, term))

list1 = [1, 2, 1, 2, 1]
term = 1
print(find_indexes(list1, term))
