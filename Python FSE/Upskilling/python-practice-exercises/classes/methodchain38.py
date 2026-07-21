class Employee:

    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        if salary <= 0:
            print("Invalid Salary")
            return self

        self.salary = salary
        return self

    def apply_raise(self, amount):
        if amount > 0:
            self.salary += amount
        return self

    def display(self):
        print("Employee Details ")
        print(f"Name   : {self.name}")
        print(f"Salary : {self.salary}")      
        return self


emp = Employee("Archana")

emp.set_salary(50000).apply_raise(5000).display()