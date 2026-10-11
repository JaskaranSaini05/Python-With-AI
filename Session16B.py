# Explore SET
# Uniqueness

john_followers = {'fionna','sia','kim','harry','geroge','sia'}
print('john_followers',john_followers)
print('type john_followers',type(john_followers))
print('lenght john_followers',len(john_followers))

numbers = list(range(10,101,10))
# convert list into set
data = set(numbers)

data.add(50)
data.add(500)
print('data:',data)

john_followers = {'fionna','sia','kim','harry'}
jack_followers = {'anna','sia','kia'}
fionna_followers = {'joe','kim'}

mutual_followers = john_followers.intersection(fionna_followers)
print('mutual_followers:',mutual_followers)