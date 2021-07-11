#Write your function here
def exponents(base, exponent):
    answer =[]
    for num in base:
        for ex in exponent:
            a = num ** ex
            answer.append(a)
    return answer


#Uncomment the line below when your function is done
print(exponents(range(1,11), range(1,6)))