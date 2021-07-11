# accepts 2 inputs: sentence, number
# function returns True if every word in sentence has a greter lenght than or equal to the number provided.

# Write your x_length_words function here:

def x_length_words(sentence, number):
    split = sentence.split()
    for word in split:
        if len(word) < number:
             return False
    return True


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True