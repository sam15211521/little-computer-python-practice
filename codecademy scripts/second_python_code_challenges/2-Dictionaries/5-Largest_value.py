#finds maximum value in dictionary
#returns the associated key

# Write your max_key function here:

def max_key(dic):
    maxkey = float('-inf')
    maxvalue =float('-inf')
    for key, value in dic.items():
        if dic[key] > maxvalue:
            maxvalue = dic[key]
            maxkey = key
    return maxkey


# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"