# Function: It performs square of a number
def square(number):
    result = number*number
    return result
print('square is',square)
print('hashcode of square is',id(square))
print('type of square is',type(square))


def square(number1,number2):
    result =  number1 * number2
    return result
print('square is',square)

# square(10) # 100 # error as old function does not exist
output = square(10,20)
print('result from square is',output)