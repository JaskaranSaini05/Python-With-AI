"""
1.Think of an Object
Song: name,artists,album,duration

"""
#2. Create its class

class Song:
    def __init__(self):
        print('constructor executed')
        print('self:',self,type(self),id(self))

# 3. Create Object from Class Defiinition
# johns_song: is not object.It is  reference variable
# It will hold hashcode of an object in memory
# Song(): creating an object in RAM(Heap Area)
johns_song = Song()
print('johns_song:',johns_song,type(johns_song),id(johns_song))

print('Data in object referred by johns_song')
print(vars(johs_song))