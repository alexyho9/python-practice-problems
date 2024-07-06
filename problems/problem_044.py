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
    result = []
    for item in key_list:
        # print(dictionary.get(item))
        result.append(dictionary.get(item))
    return result


k1 = ["name", "age"]
d1 = {"name": "Noor", "age": 29}
k2 = ["eye color", "age"]
d2 = {"name": "Noor", "age": 29}
k3 = ["age", "age", "age"]
d3 = {"name": "Noor", "age": 29}

print(translate(k1, d1))    # ["Noor", 29]
print(translate(k2, d2))    # [None, 29]
print(translate(k3, d3))    # [29, 29, 29]
