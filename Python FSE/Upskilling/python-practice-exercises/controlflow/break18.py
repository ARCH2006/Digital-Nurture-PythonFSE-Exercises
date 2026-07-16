# Break Statement
def first_even(start,end):
    if(start > end):
        print("start value must be <= end value")
        
    for i in range(start,end+1):
        if i%2==0:
            print(i)
            break
        
    else:
        print("no even numbers")
        
start = int(input())
end = int(input())
first_even(start,end)