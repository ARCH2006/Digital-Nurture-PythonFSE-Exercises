def coomon_skills(skills1,skills2):
    if not skills1 or not skills2:
        print("skill sets cannot be empty")
        
    common = skills1 & skills2
    print(common)
    
employee1 = {"python","sql","java"}
employee