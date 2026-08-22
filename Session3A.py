# Multi Value Container: List -> Mutable(We can change values)
names = ["john","jennie","kim"]
print(names,type(names),id(names))

followers = names
print(followers,type(followers),id(followers))
print(names[1],type(names[1]),id(names[1]))

followers[1] = "george"
print(followers,type(followers),id(followers))
print(names,type(names),id(names))
print(names[1],type(names[1]),id(names[1]))