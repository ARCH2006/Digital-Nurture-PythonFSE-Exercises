class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))

    def display(self):
        print("Employee Details")
        print(f"Name   : {self.name}")
        print(f"Salary : {self.salary}")
       

# Main Program
emp = Employee.from_string("Shubh,75000")

emp.display()