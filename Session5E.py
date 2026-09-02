# List indexes  0        1        2      3      4
usernames =  ['john','jennnie','fionna','kia','leo']
search = input("Enter username to search:")

# for loop
flag = False
for index in range(0,5,1):
    if usernames[index] == search:
        print('User Found',search)
        flag = True

    index +=1;
if flag == False:
    print('user not found')