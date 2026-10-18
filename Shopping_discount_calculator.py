
"""
Project 10: Shopping Discount Calculator

Create a function called calculate_discount(price).

Requirements:
1. If the price is 5000 or more, give a 20% discount.
2. If the price is 2000 or more but below 5000, give a 10% discount.
3. If the price is below 2000, give no discount.
4. Calculate the discount amount.
5. Calculate the final price after discount.
6. Print the original price, discount amount, and final price.
7. If the price is negative, print "Invalid price".

Test your function with:
calculate_discount(6000)
calculate_discount(3000)
calculate_discount(1000)
calculate_discount(-500)

Expected results:
6000 -> Discount: 1200, Final price: 4800
3000 -> Discount: 300, Final price: 2700
1000 -> Discount: 0, Final price: 1000
-500 -> Invalid price

Total marks: 10
"""
def calculate_discount(price):
    if price < 0:
        print("Invalid price")
    elif price >= 5000:
        discount = 20/100 * price
        Final_price = price - discount
        print(price,"-> Discount:",discount,"Final price:",Final_price)
    elif price >= 2000 and price <5000:
        discount = 10/100 * price
        Final_price = price - discount
        print(price,"-> Discount:",discount,"Final price:",Final_price)
    elif price < 2000:
        discount = 0
        Final_price = price - discount
        print(price,"-> Discount:",discount,"Final price:",Final_price)
        
calculate_discount(6000)
calculate_discount(3000)
calculate_discount(1000)
calculate_discount(-500)