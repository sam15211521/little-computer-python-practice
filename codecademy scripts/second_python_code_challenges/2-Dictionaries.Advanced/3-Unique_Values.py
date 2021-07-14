# reads a dict as input
#looks for unique values
#returns a number which is the count of all values from the dict without including duplicates


# Write your unique_values function here:

def unique_values(dic):
    values =[]
    for value in dic.values():
        if value not in values:
            values.append(value)
    return len(values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1