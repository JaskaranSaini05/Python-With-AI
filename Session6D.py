numbers = [10,17,23,435,9,12,]
ipl_scores = [111,210,120,95,56,54]
product_prices = [110,50,77,11,32,11,200,75,33,55]

max_number = numbers[0]
for index in range(1,len(numbers)):
    print('max_number',max_number)
    if numbers[index] > max_number:
        max_number = numbers[index]

print('numbers',max_number)

max_number = ipl_scores[0]
for index in range(1,len(ipl_scores)):
    print('max_number',max_number)
    if ipl_scores[index] > max_number:
        max_number = ipl_scores[index]
print('Ipl_scores',max_number)


max_number = product_prices[0]
for index in range(1,len(product_prices)):
    print('max_number',max_number)
    if product_prices[index] > max_number:
        max_number = product_prices[index]
print('Product_prices',max_number)
