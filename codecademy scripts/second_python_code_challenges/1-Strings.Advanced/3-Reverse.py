# Take the string given and going throug it make a new string but in reverse


# Write your reverse_string function here:

def reverse_string(string):
    reverse = ''
    i = -1
    for letter in string:
        reverse += string[i]
        i +=-1
    return reverse



#or

def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):    #range( len(word)-1,    -1,          -1)
    reverse += word[i]                    #     start here      stop here;  increments
  return reverse


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print