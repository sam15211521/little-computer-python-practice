def divisible_by_ten(num):
    remainder = num %10
    if remainder == 0:
        return True
    if remainder != 0:
        return False

# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False
