# module
import math
def area_of_circle(radius):
    if radius<=0:
        print("radius cannot be negative")
    area = math.pi * radius**2
    print(f"Area: {area:.2f}")
    
radius = 5
area_of_circle(radius)
    
 
    
        