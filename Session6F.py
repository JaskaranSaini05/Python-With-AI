def max_in_list(data):
    max_number = data[0]
    for index in range(1,len(data)):
        print('max_number',max_number)
        if data[index] > max_number:
            max_number = data[index]
    print('data',max_number)

numbers = [10,17,23,435,9,12,]
ipl_scores = [111,210,120,95,56,54]
product_prices = [110,50,77,11,32,11,200,75,33,55]

max_in_list(numbers)
max_in_list(ipl_scores)
max_in_list(product_prices)

