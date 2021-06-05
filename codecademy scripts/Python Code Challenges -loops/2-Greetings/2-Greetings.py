#Write your function here

def add_greetings(names):
    greeting =[]
    for name in names:
        a = "Hello " + name
        greeting.append(a)
    return greeting
  #funciong below returns every letter in its own area of a list  
def add_greetings2(names):
    greeting =[]
    for name in names:
        a = "Hello " + name
        greeting += a
        return greeting


#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))