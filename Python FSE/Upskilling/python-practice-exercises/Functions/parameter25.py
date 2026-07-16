def add(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Both inputs must be numbers."
    
    return a+b

result = add(5, 3)

print(f"Sum = {result}")
