"""
PERSONAL EXPENSE MANAGER

Create 3 functions:

1. add_expense(expenses, amount)
   - If amount <= 0, print "Invalid amount".
   - Otherwise, add the amount to the list.
   - Print "Expense added".

2. show_expenses(expenses)
   - If the list is empty, print "No expenses found".
   - Otherwise, display all expenses.
   - Calculate and print the total.
   - Calculate and print the average.

3. highest_expense(expenses)
   - If the list is empty, print "No expenses found".
   - Otherwise, display the highest expense.

MAIN PROGRAM:
- Create an empty list called expenses.
- Add 100, 250, and 50 using add_expense().
- Try adding -20.
- Call show_expenses().
- Call highest_expense().

EXPECTED RESULTS:
Expenses: [100, 250, 50]
Total: 400
Average: 133.33 (approximately)
Highest expense: 250

The negative amount must not be added.

MARKS: 20
- Function definitions and parameters: 4
- Adding expenses and validation: 4
- Display and total: 4
- Average calculation: 3
- Highest expense and empty-list handling: 3
- Test cases: 2
"""

def add_expense(expense,amount):
    if amount <= 0:
        print("Invalid amount")
    else:
        expense.append(amount)
        print("Expense added",amount)


def show_expenses(expense):
    if not expense:
        print("No expenses found")
    else:
        print(expense)
        total = sum(expense)
        print("total",total)
        average = sum(expense) / len(expense)
        print("average",average)
        
def highest_expense(expense):
    if not expense:
        print("No expenses found")
    else:
        max_expense = max(expense)
        print("Maximum expense:",max_expense)

expense = []
add_expense(expense,250)
add_expense(expense,100)
add_expense(expense,-20)
add_expense(expense,50)
show_expenses(expense)
highest_expense(expense)

