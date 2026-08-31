# List supports duplicates 

followers = ['john','jennie','jim','jack','jennie']
print('followers:')
print(followers,type(followers),id(followers))

for name in followers:
    print(name)


# Sets Support Uniqueness It wonot work on indexing
# technique .It uses hashing hence ,the output will be
# unoreded because of hashing

followers = {'john','jennie','jim','jack','jennie'}
print('followers now:')
print(followers,type(followers),id(followers))

fioona_followers = {'sia','kim','joe','jennie'}
print('fioona_followers:')
print(fioona_followers,type(fioona_followers),id(fioona_followers))

# mutual_followers = followers.interesection(fioona_followers)
mutual_followers = followers&fioona_followers
print('mutual_followers:')
print(mutual_followers,type(mutual_followers),id(mutual_followers))

# You can always real all the elements, but cannot capture single
# single element from set as indexing is not allowed
# print(fioona_followers[0]) #error

# for loop
# for name(we can write anyhting here ) in fioona_followers
# print(name)
for name in fioona_followers:
    print(name)