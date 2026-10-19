
# Project 2: Flexible Shopping Bill
# Topic: *args
#
# Objective:
# Create a shopping bill calculator that accepts any number
# of item prices and calculates the total bill.
#
# Requirements:
# 1. Create a function named shop_bill().
# 2. Use *args to accept any number of prices.
# 3. Print all the prices received.
# 4. Calculate and print the total bill.
# 5. Calculate and print the number of items.
# 6. If no prices are provided, print a suitable message.
#
# Test cases:
# shop_bill(100)
# shop_bill(100, 200)
# shop_bill(100, 200, 50, 25)
# shop_bill()
#
# Bonus:
# Calculate the average price of the items.
#
# Rules:
# - Use a function.
# - Use *args.
# - Do not use a fixed number of parameters.
# - Write the solution yourself.

def shop_bill(*prices):
    if not prices:
        print("No items")
        return
    print("Item prices:",prices)
    total_items = len(prices)
    print(total_items)
    total = sum(prices)
    print("Total bill:",total)
    averagee = total / total_items
    print("Average price:",averagee)
    
    
shop_bill(100)
shop_bill(100, 200)
shop_bill(100, 200, 50, 25)
shop_bill()