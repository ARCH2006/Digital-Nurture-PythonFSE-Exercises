def divde(a,b):
    try:
        result = a/b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print("cannot divide by zero")
           
divde(10,0)  