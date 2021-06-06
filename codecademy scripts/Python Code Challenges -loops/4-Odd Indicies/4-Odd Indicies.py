#Write your function here

def odd_indices(lst):
    lst2 = []
    i = 0
    for num in lst:
        if i %2 != 0:
            lst2.append(num)
            i += 1
        else:
            i +=1
    return lst2

def odd_indices2(lst):
    lst2 =[]
    for i in range(1, len(lst),2):
        lst2.append(lst[i])
    return lst2
            
            
#Uncomment the line below when your function is done
print(odd_indices2([4, 3, 7, 10, 11, -2]))