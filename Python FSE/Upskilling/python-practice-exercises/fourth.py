# Floor Division
def floorDiv(total_bill,people):
    if(total_bill<0):
        return "bill cannot be negative"
    if not isinstance(people,int) or (people <=0):
        return "Invalid number of people"
    share = total_bill // people
    return f"Each person should pay: Rs.{share}"

total_bill = 1250
people = 4
result = floorDiv(total_bill,people)
print(result)