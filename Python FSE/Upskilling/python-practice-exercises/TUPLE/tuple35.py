def print_coordinates(coordinates):
    if len(coordinates) != 2:
        print("Coordinate must contain exactly 2 values")
        return
    x,y = coordinates
    print(coordinates) 
    print(f"x coordinate: {x}")
    print(f"y coordinate: {y}")
    
    
coordinates = (15,25)
print_coordinates(coordinates)