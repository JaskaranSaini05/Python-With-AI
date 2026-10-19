"""
Goal: Save multiple student records in students.txt and display them later.
Requirements
1. Show a menu: Add student, View students, Exit.
2. Add student: Ask for name and marks, then append them to students.txt.
3. View students: Read the file and display all saved student records.
4. Exit: Use break to stop the loop.
5. Save each student's record on a separate line.
Example file content:
Jaskaran,85
Aman,92
Rahul,78


Hints
- Use while True and if/elif.
- Use input() for name and marks.
- Use "a" to add records without deleting existing ones.
- Use "\n" to separate records.
- Use "r" and file.read() to view the records.
"""

while True:
    print("option 1 add student")
    print("option2 view students")
    print("exit")
    n = int(input("Enter your option"))
    
    if n == 1:
        name = input("please enter your name")
        marks = int(input("please enter your marks"))
        with open("student.txt","a") as file:
            file.write(name + "," + str( marks) + "\n")
    elif n ==2:
        with open("student.txt","r") as file:
            print(file.read())
    elif n == 3:
        break
    else:
        print("invalid option")
    
    