# add first 2 inputs
# subtract 3 & 4
# a= multiply 1 &2
# remainder a/1

# Write your lots_of_math function here:

def lots_of_math(num1, num2, num3, num4):
    add = num1 + num2
    sub = num3 - num4
    mult = num1 * num2
    remainder =mult % num1
    print(add)
    print(sub)
    print(mult)
    print(remainder)
    return remainder

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0