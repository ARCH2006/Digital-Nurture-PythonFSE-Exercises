# Multiple Assignment
def unPack(point):
    x,y = point
    if not isinstance(x,(int,float)):
        return f"Invalid x coordinate"
    if not isinstance(y,(int,float)):
        return f"Invalid y coordinate"
    return f"x- coordinate is {x} y-coordinate is {y}"

point = 1,2
result = unPack(point)
print(result)