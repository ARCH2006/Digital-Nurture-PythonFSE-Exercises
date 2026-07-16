from math import *

def math_operations(number):
    if number <0:
        print("Number cannot be negative")
        return
    print(f"Square Root : {sqrt(number):.2f}")
    print(f"Square : {pow(number, 2)}")
    print(f"Value of Pi : {pi:.2f}")
    
number = 9
math_operations(number)
    