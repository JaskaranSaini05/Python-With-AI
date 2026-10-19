"""
===== PERSONAL DIARY =====
1. Write a new diary entry
2. View all diary entries
3. Add another entry
4. Exit

Enter your choice: 1
Write your entry: Today I learned file handling!
Entry saved successfully!
"""

while True:
    print("Option 1: write an entry to diary.txt.")
    print("Option 2: read and display the saved diary.")
    print("Option 3: append a new entry without deleting old entries.")
    print("Option 4: exit the program.")
    n = int(input("Enter your option what you want to do"))
    if n == 1:
        entry = input("write your diary entry:")
        with open("diary.txt","w") as file:
            file.write(entry)
    elif n == 2:
        with open("diary.txt","r") as file:
            print(file.read())
    elif n == 3:
        entryy = input("write a new entry")
        with open("diary.txt","a") as file:
            file.write(entryy)
    elif n == 4:
        break
    else:
        print("invalid option")