# compaires two lists of the same size
#if lsits are not same size, return: 'error: not same size'
# goes through each list and compares each value
# if values are == then record the index in a list
#Write your function here

def same_values(lst1, lst2):
    i = 0
    lst_return = []
    if len(lst1) == len(lst2):
        while i < len(lst1):
            if lst1[i] == lst2[i]:
                lst_return.append(i)
                i +=1
            else:
                i +=1
        return lst_return
    else:
        return "Error: lists not same size"

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
