# a function to multiply a number by another number
# does not work well, way to complicated and cannot use for larger numbers
def multiplication(num, time):
    product = 0
    times =list(range(time))
    i =0
    while i <= len(times)-1:
        product += num
        i +=1
    print(product)
#function for choosing what type of operation is to be done
    
cyt = choose_your_type =input("What type of operation do you want? ad, sub, mul, div: ")
    
if cyt == "mul":
    multiplication(int(input("choose your number: ")), int(input("choose your multiplicator: ")))
else:
    print("not yet made")
    

