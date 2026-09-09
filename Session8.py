# Default Arguments
# You can give default values from right to left
# def add(number1=10,number2): error
# def add(number1,number2=100): correct

def add(number1=10,number2=20):
    result = number1 + number2
    return result

result_from_add=add()
print(result_from_add)