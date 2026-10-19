
# Project 3: Student Profile Builder
# Topic: **kwargs
#
# Objective:
# Create a function that accepts any number of named
# student details and displays them in a readable format.
#
# Requirements:
# 1. Create a function named student_profile().
# 2. Use **kwargs to accept flexible named details.
# 3. Print each detail's name and value.
# 4. Print the total number of details provided.
# 5. If no details are provided, print a suitable message.
#
# Test cases:
# student_profile(name="Jaskaran")
# student_profile(name="Jaskaran", age=20)
# student_profile(name="Jaskaran", age=20,
#                 course="Python", city="Ludhiana")
# student_profile()
#
# Bonus:
# If a "skills" detail is provided, display it separately.
#
# Rules:
# - Use a function.
# - Use **kwargs.
# - Do not hardcode a fixed number of parameters.
# - Write the solution yourself.


def student_profile(**details):
    if not details:
        print("Sorry no details found")
        return
    print("\nStudent Profile")
    for key,value in details.items():
        print(key,":",value)
    print("total details:",len(details))
student_profile(name="Jaskaran")
student_profile(name="Jaskaran", age=20)
student_profile(name="Jaskaran", age=20, course="Python", city="Ludhiana")
student_profile()