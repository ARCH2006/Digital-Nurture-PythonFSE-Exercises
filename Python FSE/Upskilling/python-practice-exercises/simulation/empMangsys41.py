import json

class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Salary: {self.salary}"
    
class EmployeeManager:
    def __init__(self):
        self.employees = {}
        
    def add_employee(self,employee):
        self.employees[employee.emp_id] = employee
    
    def save_to_file(self):
        data = {}
        for emp_id,employee in self.employees.items():
            data[emp_id] = {
                "name" : employee.name,
                "salary" : employee.salary
            }
        with open("emps.json","w") as file:
            json.dump(data,file,indent = 4)
        
        print("Employees added successfully")
        
    def load_from_file(self):
        try:
            with open("emps.json","r") as file:
                read_data = json.load(file)
            self.employees.clear()
            
            for emp_id,details in read_data.items():
                employee = Employee(int(emp_id),details["name"],details["salary"])
                
                self.employees[int(emp_id)] = employee
                
            print("Employees loaded successfully.")
    
        except FileNotFoundError:
            print("File not found.")
            
    def display_employees(self):
        for employee in self.employees.values():
            print(employee)
            
            
            
manager = EmployeeManager()
manager.add_employee(Employee(101, "Archana", 50000))
manager.add_employee(Employee(102, "Priya", 65000))
manager.add_employee(Employee(103, "Rahul", 55000))

manager.save_to_file()

manager.load_from_file()

manager.display_employees()
                  
        