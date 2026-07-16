# Min/Max Functions 
def minMax(salaries):
    if salaries == []:
        return "Salary list is empty"
    lowest_salary = min(salaries)
    highest_salary = max(salaries)
    print(f"Lowest Salary : {lowest_salary}")
    print(f"Highest Salary: {highest_salary}")

list_of_num = [50000, 75000, 62000, 95000]
result = minMax(list_of_num)
print(result)