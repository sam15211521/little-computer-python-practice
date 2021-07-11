#removes all elements from a list with an index within a range
#accepts a list, start, ending

#Write your function here

def remove_middle(lst, start, ending):
    front = lst[: start]
    back = lst [ending+1:]
    final = front + back
    return final


#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))