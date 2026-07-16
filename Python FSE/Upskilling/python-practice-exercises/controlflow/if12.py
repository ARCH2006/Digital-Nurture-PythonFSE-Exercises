# Simple If
def check_pass(marks):
    if marks>=35:
        return "Pass"
    else:
        return "Fail"
marks = int(input("enter student marks"))
print(check_pass(marks))