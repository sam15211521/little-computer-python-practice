#Write your function here
#looks at a a list and removes any even numbers until it hits an odd number
def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] %2 ==0):
        lst.remove(lst[0])
    return lst


#this function deletes all evens from a list
def delete_evens(lst):
    lst2 =[]
    i = 0
    for num in lst:
        if num %2!=0:
            
            lst2.append(lst.pop(i))
            i+= 1
            
        else:
            i+=1
            continue
    return lst2
    

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))