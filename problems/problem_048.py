# Write a function that meets these requirements.
#
# Name:       count_word_frequencies
# Parameters: sentence, a string
# Returns:    a dictionary whose keys are the words in the
#             sentence and their values are the number of
#             times that word has appeared in the sentence
#
# The sentence will contain now punctuation.
#
# This is "case sensitive". That means the word "Table" and "table"
# are considered different words.
#
# Examples:
#    * sentence: "I came I saw I learned"
#      result:   {"I": 3, "came": 1, "saw": 1, "learned": 1}
#    * sentence: "Hello Hello Hello"
#      result:   {"Hello": 3}

## FUNCTION PSEUDOCODE
# function count_word_frequencies(sentence):
def count_word_frequencies(sentence):
    # words = split the sentence
    words = sentence.split(" ")
    # counts = new empty dictionary
    counts = {}
    # for each word in words
    for w in words:
        # convert to lowercase and remove punctuation
        w = w.lower()
        w = w.replace(".", "")
        # if the word is not in counts
        if w not in counts:
            # counts[word] = 0
            counts[w] = 0
        # add one to counts[word]
        counts[w] += 1
    # return counts
    return counts


# TEST CODE
sentence1 = "Your task is to do the impossible within thirty days. You. Can. Do. It."
print(count_word_frequencies(sentence1))

sentence1 = "I came. I saw. I learned."
print(count_word_frequencies(sentence1))

sentence1 = "I eat mushrooms. You eat mushrooms. We eat mushrooms. They eat mushrooms."
print(count_word_frequencies(sentence1))
