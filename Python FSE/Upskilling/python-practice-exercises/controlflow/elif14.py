# Multi-way decision
def assign_grade(score):
    
    if score < 0 or score > 100:
        return "Invalid score! Score must be between 0 and 100."

    if score >= 90:
        grade = "A"
        
    elif score >= 75:
        grade = "B"
        
    elif score >= 50:
        grade = "C"
       
    else:
        grade = "Fail"
       
    return f"Grade: {grade}"
score = 88
print(assign_grade(score))