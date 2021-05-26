# Write your in_range function here:
# number falls in a range
# 3 parameters: num, lower, upper

def in_range(num, lower, upper):
    if num <= upper and num >= lower:
        return True
    else:
        return False







# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False