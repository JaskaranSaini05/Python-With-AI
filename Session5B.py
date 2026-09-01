coupon_code = input('Enter coupon code:')
billing_amount = int(input('Enter billing amount:'))

# Simple or Regular if/else
"""
if billing_amount > 449:
    print('coupon can be applied')
    print('thank you')
else:
    print('coupon cannot be applied')
    print('amount is low')
"""


# Nested if/else
if coupon_code == 'NOMNOW150':
    print('coupon can be applied')
    if billing_amount > 449:
       billing_amount -= 150 # billing_amount = billing amount - 150
       print('please pay',billing_amount)
       print('thank you')
    else:
        print('sorry,applied coupon is not avaible')
        print('add items worth',449-billing_amount,'more')
else:
    print('coupon cannot be applied')
