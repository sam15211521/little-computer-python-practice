# This function counts the number of times a species is in a list.
# then it compares the amount with a maximum value
# returns true if maximum value is breached
#Write your function here

def more_than_n(lst, species, n):
    if lst.count(species) > n:
        return True
    else:
        return False
#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))