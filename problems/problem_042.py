# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]
#     list2:  [ 10,   1, 180]
#     result: [110, 201, 480]
#
# Look up the zip function to help you with this problem.

def pairwise_add(list1, list2):
    # create new list
    new_list = []
    # pair up list1 and list2
    list_pair = zip(list1, list2)
    # for each tuple in list, add values together and append to new list
    for item in list_pair:
        new_list.append(item[0] + item[1])
    # return new list
    return new_list


# Example test lists
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
print(pairwise_add(list1, list2))

list1 = [100, 200, 300]
list2 = [10,   1, 180]
print(pairwise_add(list1, list2))
