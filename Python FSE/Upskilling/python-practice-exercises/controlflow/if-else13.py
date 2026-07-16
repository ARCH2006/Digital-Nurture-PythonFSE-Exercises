# Even or Odd
def evenOrOdd(num):
    if num<0 or not isinstance(num,int):
        return "invalid number"
    if num%2==0:
        return f"{num} is even number"
    else:
        return f"{num} is odd number"
number = 8
result = evenOrOdd(number)
print(result)