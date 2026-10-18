"""
SHOPPING CART TOTAL AND TAX

Create a function called calculate_cart(prices).

Requirements:
1. Accept a list of product prices.
2. If the list is empty, print "Cart is empty".
3. If any price is negative, print "Invalid price".
4. Calculate the total price of all products.
5. Calculate 18% tax on the total.
6. Calculate the final amount (total + tax).
7. Print the total, tax, and final amount.
8. Call the function with at least 3 different test cases.

Example:
calculate_cart([100, 200, 300])

Expected output:
Total: 600
Tax: 108
Final amount: 708

Another test:
calculate_cart([])

Expected output:
Cart is empty

Another test:
calculate_cart([100, -50, 200])

Expected output:
Invalid price

Marks: 10
- Function definition and parameter: 2
- Empty cart handling: 2
- Negative price validation: 2
- Correct total and tax: 2
- Final amount and test cases: 2
"""

def calculate_cart(price):
    if not price  :
        print("Cart is empty")
    elif any(p < 0 for p in price):
        print("Invalid price")
    else:
        total = sum(price)
        print("Total:",total)
        tax = 18/100 * total
        print("Tax:",tax)
        final_amount =  total + tax
        print("Final amount:",final_amount)
calculate_cart([])
calculate_cart([100, 200, 300])
calculate_cart([100, -50, 200])