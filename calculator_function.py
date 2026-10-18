"""
Create a function called calculator(a, operator, b).
It should perform calculations based on the operator provided.
Requirements
1. If the operator is "+", add the two numbers.
2. If it is "-", subtract the second number from the first.
3. If it is "*", multiply the numbers.
4. If it is "/", divide the first number by the second.
5. If the operator is invalid, print "Invalid operator".
6. If the second number is 0 and the operator is "/", print "Cannot divide by zero".

"""

def calculator(a,operator,b):
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b )
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        if b == 0 :
            print("cannot divide by zero")
            return
        print(a / b)
        
    else:
        print("Invalid operator")

calculator(10, "+", 5)
calculator(10, "-", 5)
calculator(10, "*", 5)
calculator(10, "/", 5)
calculator(10, "/", 0)	
calculator(10, "%", 5)