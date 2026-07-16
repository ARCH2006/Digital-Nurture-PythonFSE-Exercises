def calc_salary(base,bonus):
    # validating the input
    if base <0 or bonus <0:
        print("invalid input")
    # adding base and bonus to calculate total salary
    
    total = base+bonus
    print(f"salary : {total}")

# user input   
base = int(input())
bonus = int(input())
# functon calling
calc_salary(base,bonus)

    