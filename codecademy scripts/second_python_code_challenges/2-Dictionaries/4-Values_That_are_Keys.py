#A function that creates a family tree
#accepts 1 para: dic
# creates a list
#loop through dict values
#test if value is a key in the dict
#if it is move to the list
#return list

# Write your values_that_are_keys function here:

def values_that_are_keys(dic):
    parent_values = []
    for child in dic.values():
        if child in dic:
            parent_values.append(child)
    return parent_values


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]