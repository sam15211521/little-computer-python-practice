#Write your function here
# compares the amount of times two diffrent items appear
#and returns the one with the most repeated ones
def more_frequent_item(lst, item1, item2):
    if lst.count(item2) >= lst.count(item1):
        return item2
    else:
        return item1

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))