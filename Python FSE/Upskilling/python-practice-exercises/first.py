# Float Precision
def calculateNetSalary(salary,tax_rate):
    if salary<=0:
        return "Invalid salary"
    if tax_rate<0:
        return "Invalid tax rate"
    tax = salary*tax_rate
    salary -= tax
    return f"Net salary: {salary:.2f}"

salary = 75000.5
tax_rate = 0.18
result = calculateNetSalary(salary,tax_rate)
print(result)