# this function finds the largest number in a list
# set default max to first elemnent in list
#if number is greater than starting max then replace max with what is found

#Write your function here

def max_num(lst):
    maxnum = lst[0]
    for num in lst:
        if num > maxnum:
            maxnum = num
    return maxnum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))