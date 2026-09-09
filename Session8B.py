# for number in range(1,11):
#   print(number)

# Functions - replacing loops
# recursion - executing a function again and again
# execution must stop on some condition

def print_number(number):
    print(number)
    if number > 0:
        print_number(number=number-1)

print_number(number=10)