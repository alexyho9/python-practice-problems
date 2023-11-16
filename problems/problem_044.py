# Complete the translate function which accepts two
# parameters, a list of keys and a dictionary. It returns a
# new list that contains the values of the corresponding
# keys in the dictionary. If the key does not exist, then
# the list should contain a None for that key.
#
# Examples:
#   * keys:       ["name", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     ["Noor", 29]
#   * keys:       ["eye color", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [None, 29]
#   * keys:       ["age", "age", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [29, 29, 29]
#
# Remember that a dictionary has the ".get" method on it.

def translate(key_list, dictionary):
    # Create empty result list
    results = []
    # loop through key list
    for key in key_list:
        # for each key in key list, find value in dictionary
        value = dictionary.get(key)
        # add to results list
        results.append(value)
    # return final results
    return results


# Test Code
keys = ["name", "age"]
dictionary = {"name": "Noor", "age": 29}
print(translate(keys, dictionary))

keys = ["eye color", "age"]
dictionary = {"name": "Noor", "age": 29}
print(translate(keys, dictionary))

keys = ["age", "age", "age"]
dictionary = {"name": "Noor", "age": 29}
print(translate(keys, dictionary))
