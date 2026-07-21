class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

emp1 = Employee("Ramu",50000)
emp2 = Employee("Archana",50000)
emp3 = Employee("Rahul",55000)
emp1.display()
print()
emp2.display()