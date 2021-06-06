#iterates though 2 lists
# calculates the sum of each list
# returns which has the greater sum
#if both sums are the same, returns sum and statement

#Write your function here
def larger_sum(lst1,lst2):
    first = 0
    second = 0
    for num in lst1:
        first += num
    for num in lst2:
        second += num
    if first > second:
        print(first)
        return lst1
    elif second > first:
        print(second)
        return lst2
    else:
        return "sums are equal "+ str(first)


#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7,3]))