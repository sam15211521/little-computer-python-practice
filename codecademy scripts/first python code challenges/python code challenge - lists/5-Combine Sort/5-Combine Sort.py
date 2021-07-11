# this function combines two lists together, then sorts them
#Write your function here

def combine_sort(lst1, lst2):
    lstnew = sorted(lst1 + lst2)
    return lstnew


#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))