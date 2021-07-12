# Write your make_spoonerism function here:

def make_spoonerism(word1, word2):
    char1 = word1[0]
    char2 = word2[0]
    wd1 = word1[1:]
    wd2 = word2[1:]
    spoon = char2+wd1 +' ' + char1 +wd2
    return spoon
    
#or
def make_spoonerism(word1,word2):
    return word2[0]+word1[1:] + ' '+ word1[0] + word2[1:]
    

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a