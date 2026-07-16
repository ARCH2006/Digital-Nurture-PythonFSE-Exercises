# While Loop
def print_numbers(count):
    if count<=0:
        print("Error: Count must be >0")
        return
    while count>0:
        print(count)
        count-=1
number = 5
print(print_numbers(number))