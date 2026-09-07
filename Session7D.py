def square_of_number(number):
    print('1 number is:',number,id(number))
    number = number * number
    print('2 number is:',number,id(number))

number = 10
print('3 number is:',number,id(number))
square_of_number(number)
print('4 number is:',number,id(number))
