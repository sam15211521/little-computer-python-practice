# able to check if a user name is located within a greeting
# needs to accept two para: string for sentence, string for name
# return True if string for name in string

def check_for_name(greeting, name):
    if (greeting.title()).find(name.title()) !=-1:
        return True
    return False


# Write your check_for_name function here:

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False