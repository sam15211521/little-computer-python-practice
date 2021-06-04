#Write your function here
def middle_element(lst):
    if len(lst)%2 == 0:
        average = 0
        first =lst[int(len(lst)/2)-1]
        last = lst[int(len(lst)/2)]
        average = (first + last)/2
        return average
    else:
        return lst[int(len(lst)/2)]


#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))