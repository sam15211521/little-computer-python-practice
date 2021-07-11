#golden ratio summation
def append_sum(lst):
    i =0
    while i < 3: 
        sums = lst[-2] + lst[-1]
        lst.append(sums)
        i +=1
    return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
