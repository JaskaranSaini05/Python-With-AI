"""
Your task: Create a Student class that stores a student's name, age and course.

Requirements:
1. Create a class called Student.
2. Use __init__() to accept name, age and course.
3. Store them using self.
4. Create two student objects with different details.
5. Print the details of both students.
"""
class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
    
student1 = Student("Aman",20,"Python")
student2 = Student("Jaskaran",21,"Networking")
    
student1.display()
print()
student2.display()