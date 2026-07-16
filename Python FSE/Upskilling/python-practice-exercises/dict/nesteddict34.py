def retrieve_employees(data,department,employee):
    if department not in data:
        print("Error: Department not found.")
        return
    
    if employee not in data[department]:
        print("Error: Employee not found.")
        return
    salary = data[department][employee]["salary"]
    print(f"{employee} Salary     : {salary}")
        

employees = {
    "IT": {
        "Archana": {
            "salary": 50000
        },
        "Priya": {
            "salary": 48000
        }
    },
    "HR": {
        "Rahul": {
            "salary": 45000
        }
    }
}
retrieve_employees(employees,"IT","Archana") 