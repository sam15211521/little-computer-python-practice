#creates a new dictionary based on a list of strings
#keys of dict will e every string in our list of strings
#values iwll be the lenght of each of the words in the string list

# Write your word_length_dictionary function here:

def word_length_dictionary(lst):
    new_dict = {}
    for string in lst:
        length = len(string)
        new_dict[string] = length
    return new_dict


# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}