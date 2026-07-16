# Basic Input
def user_input():
    name = input("Enter your name").strip()
    if name == "":
        print("name cannot be empty")
        return 
    print(f"Hello, {name}! Welcome to Python.")
    
user_input()