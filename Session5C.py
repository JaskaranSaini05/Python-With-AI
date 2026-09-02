promo_code = input("Enter promo code:")
amount = float(input("Enter Amount:"))

# Ladder if/else
if promo_code == "zomato":
    if amount > 300:
        discount = 0.20 * amount
        bill_to_pay = amount - discount
        print("You got a discount of",discount)
        print("Your amount was",amount)
        print("Please pay ",bill_to_pay)
    else:
        print("Please add items worth",301 - amount,'to get discount')
elif promo_code == "bingo":
    if amount > 500:
        discount = 0.50 * amount
        if discount > 150 :
            discount = 150
        bill_to_pay = amount - discount
        print("You got a discount of",discount)
        print("Your amount was",amount)
        print("Please pay ",bill_to_pay)
    else:
        print("Please add items worth",501 - amount,'to get discount')
else:
    print("Invalid Coupon Code")