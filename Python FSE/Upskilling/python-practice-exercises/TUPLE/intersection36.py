def common_skills(skills1,skills2):
    if not skills1 or not skills2:
        print("skill sets cannot be empty")
        
    common = skills1 & skills2
    union = skills1 | skills2
    
    print(common)
    print(union)
employee1 = {"python","sql","java"}
employee2 = {"python","mongoDB","java"}
common_skills(employee1,employee2)
