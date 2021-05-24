username = input("Type username ")
password = ""
login_yes = ""
if username == "sam1521":
    password = input("Type password ")
    if password == "1521":
        print ("Welcome Sam Hendrix")
        login_yes = "#2A!839kdajfiwlIdj*"
    else:
        print ("invalad password")
else:
    print("invalad user name")

print(login_yes)