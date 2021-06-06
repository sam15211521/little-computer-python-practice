#takes values in a list and adds them up until 9000
#when value reaches 9000 summing ends returns value not over 9000
#Write your function here

def over_nine_thousand(lst):
    i = 0
    power =0
    
    while i < len(lst) and power <=9000:
        power += lst[i]
        i += 1
    return power -lst[i-1]


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))