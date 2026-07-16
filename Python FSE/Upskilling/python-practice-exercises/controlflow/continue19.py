# Continue stmnt

def sum_odd(size):
    if size <= 0:
        print("Range must be greater than 0")
        return
    total = 0
    
    for i in range(size):
        if i%2==0:
            continue
        print(i)
        total+=i
    print(f"Total Sum = {total}")  
    
range_size = 10
sum_odd(range_size)
    