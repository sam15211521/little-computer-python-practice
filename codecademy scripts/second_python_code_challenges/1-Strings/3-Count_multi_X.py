# accepts a string and substring to compare
# num of occurance of the second para in first para is returned
#remember the split funciton

# Write your count_multi_char_x function here:

def count_multi_char_x(word, x):
    return len(word.split(x))-1
    


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1