"""
name = input('enter your name:')
person_to_meet = input('enter  person name you want to meet:')
purpose = input('enter your purpose to meet:')

print('Data:{},{},{}'.format(name,person_to_meet,purpose))
"""
# This file read and write operation will work on flat files
# i.e. text files(eg:.txt,.md,.py,.c,.cpp,.json etc)
# it wont work for docx,pdf,pptx
file = open('Session1.py','r')
data = file.read()
print(data)

lines = file.readlines()
print(lines)