# 1. define funciton to accept 1 parameter (word whose letters we count
# 2. create counter
# 3. loop
# 4 return the count of unique characters

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Write your unique_english_letters function here:

def unique_english_letters(word):
    letter_counter = []
    for letter in word:
        if letter not in letter_counter:
            letter_counter.append(letter)
    return len(letter_counter)

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters(letters))