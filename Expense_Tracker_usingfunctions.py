
"""
Project 9: Expense Tracker

Create a function called track_expenses(expenses).

Requirements:
1. Accept a list of expenses.
2. Calculate the total amount spent.
3. Find the highest expense.
4. Find the lowest expense.
5. Calculate the average expense.
6. Print all four results.

Test your function with:
track_expenses([100, 250, 50, 400, 200])

Expected output:
Total expenses: 1000
Highest expense: 400
Lowest expense: 50
Average expense: 200

Total marks: 10
"""
  
def track_expenses(expense):
    total_expense = sum(expense)
    print("Total expense:",total_expense)
    
    max_number = max(expense)
    print("Highest expense:",max_number)
    
    min_number = min(expense)
    print("lowestt expense:",min_number)
    
    average = sum(expense) / len(expense)
    print("Average expense:",average)
    
track_expenses([100, 250, 50, 400, 200])
