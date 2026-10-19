"""
Concept first: You can read a file line by line and count how many lines and words it contains.
- file.read() reads the entire file.
- .split() separates text into words.
- .splitlines() separates text into lines.
- len() counts the items.
Your task
Create a program that reads article.txt and displays the number of words, lines, and characters.

Example article.txt:
Python is easy.
I am learning file handling.
I love coding.


Expected output:
Total words: 10
Total lines: 3
Total characters: 57


Requirements
1. Open article.txt in read mode ("r").
2. Read all its content.
3. Count the words.
4. Count the lines.
5. Count the characters.
6. Display all three totals.
Hints, bro:
content = file.read()



- Words: len(content.split())
- Lines: len(content.splitlines())
- Characters: len(content)
"""
with open("article.txt","w") as file:
    file.write("Python is easy I am learning file handling.I love coding.")
    
with open("article.txt","r") as file:
    content = file.read()
    print(content)
words = len(content.split())
print("Total word:",words)

wordss = len(content.splitlines())
print("Total lines:",wordss)