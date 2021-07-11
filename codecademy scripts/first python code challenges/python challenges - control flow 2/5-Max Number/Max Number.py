# Write your max_num function here:
def max_num(num1, num2, num3):
    ties = "It's a tie!"
    
    if num1 > num2 and num1 > num3:
        
        if num1 == num2 or num1 == num3:
            return ties
        else:
            return num1
    elif num2 > num1 and num2 > num3:
        
        if num2 == num1 or num2 == num3:
           return ties
        else:
            return num2
        
    elif num3 > num1 and num3 > num2:
        if num3 ==num1 or num3 == num2:
           return ties
        else:
            return num3
        
    else:
        return ties
    

# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(4, 3, 4))
# should print "It's a tie!"