"""
Your mission: Build a program that accepts student marks, calculates the average, and displays the result.

Requirements
1. Ask the user for their name.
2. Ask for marks in 3 subjects.
3. Store the marks in variables.
4. Create a function called calculate_average() to calculate the average.
5. Create a function called get_grade() to determine the grade.
6. Display the student's name, total marks, average, and grade.
7. Use if, elif, and else to determine the grade.
"""

name = input("Enter your name:")
mathh = float(input("Enter your math scores:"))
history = float(input("Enter your history scores:"))
science = float(input("Enter your science scores:"))

def calculate_average(mathh,history,science):
    total_marks = mathh + history + science
    average = total_marks / 3
    return total_marks,average
    
def get_grade(average):
    if average > 80:
        print("Grade A")
    elif average > 60 and average < 80:
        print("Grade B")
    elif average > 50 and average < 60:
        print("Grade C")
    else:
        print("Grade D")
total_marks,average = calculate_average(mathh,history,science)
grade=get_grade(average)