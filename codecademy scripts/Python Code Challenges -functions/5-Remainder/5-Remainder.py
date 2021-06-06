# finds the remainder of two numbers when performing mathematical operations on them.
# multipy the number by 2 and devide by 2 the add the two together and deivde them
#return the remainder

# a*2  % b/2 = return
# Write your remainder function here:

def remainder(num1, num2):
    a = num1*2
    b = num2/2
    ans = a%b
    return ans


# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0