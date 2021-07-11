#extracts every other letter from a stirng and returns the resulting string
# Write your every_other_letter function here:

def every_other_letter(string):
    i =0
    String =''
    for letter in string:
        if i %2 == 0:
            String += letter
            i+=1
        else:
            i+=1
    return String


#       or


def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 