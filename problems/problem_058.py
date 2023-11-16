# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
#
# In the items in the input, there will only be one comma.
#
# Examples:
#     * input:   ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
#     * input:   ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
#     * input:   ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string.

def group_cities_by_state(city_state_list):
    # check if input is in list format
    if type(city_state_list) != list:
        raise ValueError
    # create empty dict to store output
    result = {}
    # loop through list items
    for city_state in city_state_list:
        # separate city and state and remove whitespace
        city = city_state.split(",")[0].strip(" ")
        state = city_state.split(",")[1].strip(" ")
        # create dictionary entry if new state
        if state not in result:
            result[state] = []
        # append city to value of state key
        result[state].append(city)
    # return final dictionary
    return result


# Test Code
city_state_list = ["Manchester, MA", "Boston, MA", "Lexington, MA", "Redding, CA"]
print(group_cities_by_state(city_state_list))

city_state_list = ["Tucson, AZ", "Houston, TX", "Denver, CO", "Las Vegas, NV", "Austin, TX", "Dallas, TX", "Sparks, NV"]
print(group_cities_by_state(city_state_list))
