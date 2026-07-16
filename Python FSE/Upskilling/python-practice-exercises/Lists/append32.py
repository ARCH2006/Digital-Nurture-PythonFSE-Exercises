def add_expense(expenses,amnt):
    if amnt<=0:
        print("Expense must be greater than 0")
        return 
    expenses.append(amnt)
    print("Updated Expenses:", expenses)
    
expenses = [500, 750, 1200]

add_expense(expenses, 300)