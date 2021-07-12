# look up the values in dict
# adds the values together


# Write your sum_values function here:

def sum_values(dic):
    summ =0
    for value in dic.values():
        summ += value
    return summ


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6