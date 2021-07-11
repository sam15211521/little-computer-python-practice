# extracts a portion of string between two characters
# three para: 1)the string, 2) the starting character of the substring, 3) the ending character
#find the starting character and find the ending character

# Write your substring_between_letters function here:

def substring_between_letters(string, start, end):
    first_index = string.find(start)
    second_index =string.find(end)
    if first_index != -1 and second_index !=-1:
        substring = string[first_index+1:second_index]
    else:
        substring = string
    return substring
            


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"