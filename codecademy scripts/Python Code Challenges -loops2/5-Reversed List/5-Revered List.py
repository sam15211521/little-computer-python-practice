# looks thorugh a 2 lists
# compaires them in opposite directions
# if same true
# if not false

#Write your function here

def reversed_list(lst1, lst2):
    index = 0
    rindex =-1
    for i in range(len(lst1)):
        if lst1[index] == lst2[rindex]:
            index +=1
            rindex += -1
        else:
            return False
    return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))