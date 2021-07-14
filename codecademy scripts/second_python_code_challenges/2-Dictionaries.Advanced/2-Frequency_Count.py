#counts the frequency of each string in the list of strings (frequency)
# accepts a list of strings as input and returns a new dictionary:

# Write your frequency_dictionary function here:

def frequency_dictionary(lst):
    dic ={}
    for entry in lst:
        if entry in dic:
            dic[entry] += 1
        else:
            dic[entry] =1
    return dic

#or

def frequency_dictionary(lst):
    dic ={}
    for entry in lst:
        if entry not in dic:
            dic[entry] = 0
        
        dic[entry] +=1
    return dic



# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}