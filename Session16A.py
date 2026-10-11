# List Data Structure in Python

numbers = list(range(10,101,10))
print('numbers',numbers)

numbers.append(99)
numbers.append(77)
numbers.append(111)
numbers.append(11)


print('numbers',numbers)

print('length of numbers',len(numbers))
print('Sum of numbers',sum(numbers))
print('Min of numbers',min(numbers))
print('Max of numbers',max(numbers))
print('Avg of numbers',sum(numbers)/len(numbers))

data = tuple(numbers)
print('data',data)

reverse_numbers = list(reversed(numbers))
print(reverse_numbers)

# Create a function which takes input a list and returns a list of reverse numbers
# Create a function which takes input a list and reverse numbers in the same list

idex = numbers.index(40)
print('idx is:',idex)

data = [10,20,43,5,6,3,200]
data.sort()
print(data)

data.remove(6)
print(data)

data1 = [10,20,30,40,50]
print('data1',data1)
data1.pop()
print('data1 after pop',data1)