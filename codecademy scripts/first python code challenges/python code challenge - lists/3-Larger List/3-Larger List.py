#Write your function here
# this function determines which lst is larger and moves the last entry to the other list. moves the last item in a list to 
def moving_larger_list(lst1, lst2):
    def moves():
        item = lst1[-1]
        lst1.pop()
        lst2.append(item)
        return lst1, lst2
    if len(lst1) > len(lst2):
        while len(lst1) > len(lst2):
            moves()
            return lst1, lst2

    elif len(lst2) > len(lst1):
        while len(lst2) > len(lst1):
            item = lst2[-1]
            lst2.pop()
            lst1.append(item)
            return lst1, lst2
    else:
        return "Both are the same length", lst1, lst2
        

#Uncomment the line below when your function is done
#print(moving_larger_list([4, 10, 2], [-10, 2, 5, 10]))

#Write your function here
# this function determines if one list is larger.
# returns the last entry of the larger list
# if both lists are the same size: return last lst1

def larger_list(lst1, lst2):
    if len(lst1) > len(lst2):
        return lst1[-1]
    elif len(lst2) > len(lst1):
        return lst2[-1]
    else:
        return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# more elegant code:
def shorter_larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

