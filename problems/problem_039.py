# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}

def reverse_dictionary(dictionary):
    # create new empty dictionary
    new_dict = {}
    # for each key in original dictionary, add value and key
    for key in dictionary:
        # get value
        value = dictionary[key]
        new_dict[value] = key

    # return new dictionary
    return new_dict


dict_a = {"one": 1, "two": 2, "three": 3}
dict_b = {"uno": "하나", "dos": "둘", "tres": "셋", "cuatro": "넷"}

print(reverse_dictionary(dict_a))
print(reverse_dictionary(dict_b))
