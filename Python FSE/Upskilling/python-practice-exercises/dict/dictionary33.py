def updateDictionary(emp1,emp2):
    if not emp1 or not emp2:
        print("employee data cannot be empty")
        return 
    
    emp1.update(emp2)
    print(emp1)
  
    
employee1 = {
    "id":1,
    "name":"John"
    
}
employee2 ={
    # "id":2,
    # "name":"Alice"
    "dept":"fse",
    "salary":50000
}
updateDictionary(employee1,employee2)
    