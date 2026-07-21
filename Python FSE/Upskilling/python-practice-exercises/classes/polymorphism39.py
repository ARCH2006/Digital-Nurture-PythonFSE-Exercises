class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer write code")
        
class Manager(Employee):
     def work(self):
        print("Manager manages the team.")
employees = [
    Developer(),
    Manager(),
    Employee()
]


for emp in employees:
    emp.work()    