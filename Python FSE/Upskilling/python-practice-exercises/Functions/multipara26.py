def area_of_rectangle(length,breadth):
    if length <= 0 or breadth <= 0:
        return "invalid input"
    area = length * breadth
    return f"Area: {area}"

result = area_of_rectangle(5,3)
print(result)
