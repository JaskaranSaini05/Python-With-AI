
# LESSON: Understanding dictionary .items()
#
# Error:
# TypeError: dict.items() takes no arguments (1 given)
#
# Why did this happen?
# details.items(0) is incorrect because .items() does not accept
# an index or any arguments.
#
# Correct usage:
# details.items() → returns all key-value pairs in the dictionary.
#
# Example:
# details = {"name": "Jaskaran", "age": 20}
#
# for key, value in details.items():
#     print(key, ":", value)
#
# Output:
# name : Jaskaran
# age : 20
#
# Remember:
# details.keys()   → returns all keys
# details.values() → returns all values
# details.items()  → returns all key-value pairs
#
# LESSON: Git
# git add → stages the file
# git commit → saves a snapshot locally
# git push → uploads the commit to GitHub


school_name = "ABC School"
total_students = 0

def show_marks(name,marks):
    student_name = name
    print("School:",school_name)
    print("Student:",student_name)
    print("Marks:",marks)
    print()
    
def update_total():
    global total_students
    total_students += 1
    
show_marks("Jaskaran", 85)
show_marks("Aman", 92)

update_total()
update_total()

print("Total students:", total_students)