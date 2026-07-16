# Nested If
def login(user,pwd):
    if user == "" or pwd == "":
        return "Invalid input"
    
    if user == "admin":
        if pwd == "pass123":
            return "Login successfull"
        else:
            return "Incorrect password"
    else:
        return "Incorrect username"
    
user = input("enter username")
pwd = input("enter password")
print(login(user,pwd))