# Numeric Input
def calcAge():
    age = input("enter your Age")
    if not age.isdigit():
        print("Invalid input")
        return 
    age = int(age)
    print(f"Next year you'll be {age+1}")
    
calcAge()