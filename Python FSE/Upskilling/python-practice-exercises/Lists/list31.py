def printCart(items):
    if len(items) == 0:
        print("cart is empty")
    print(items)
    for i in items:
        print(i)
items= [100,250,75]
printCart(items)
