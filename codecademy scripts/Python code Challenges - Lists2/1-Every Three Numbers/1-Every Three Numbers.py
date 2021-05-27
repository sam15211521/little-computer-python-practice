#creates a list of number up to 100 in increments of 3 starting from n
#Write your function here
def every_three_nums(start):
    lst = list(range(start, 101, 3))
    return lst


#Uncomment the line below when your function is done
print(every_three_nums(91))