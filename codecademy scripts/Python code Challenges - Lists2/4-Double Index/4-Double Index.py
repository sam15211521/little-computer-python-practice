#Write your function here
#doubles the value at a given index then returns a list with that
#value in the same place

#this function modifies the origional list
def double_index(lst,index):
    if index >= len(lst):
        return "Index not available max index = "+ str(len(lst)-1)
    else:
        lst.insert(index, 2*lst[index])
        lst.remove(lst[index+1])
        return lst
    
# this one will not modify the origional list
def double_index2(lst, index):
    if index >=len(lst):
        return "Index not available. Max index = "+ str(len(lst)-1)
    else:
        start = lst[:index]
        start.append(2*lst[index])
        end = lst[index+1:]
        new_lst = start + end
        return new_lst

#Uncomment the line below when your function is done
print(double_index2([3, 8, -10, 12, 1], 5))