# loops through a dictionary and adds 10 to every value




# Write your add_ten function here:

def add_ten(dic):
    for key in dic.keys():
        dic[key] += 10
    return dic

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}