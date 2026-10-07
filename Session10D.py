class Song:
    def __init__(self,tracks,artists,album,duration):
        self.tracks = tracks
        self.artists = artists
        self.album = album
        self.duration = duration
        self.next = None
        self.previous = None
    def show(self):
        print("-------------")
        print('Track:',self.tracks)
        print('Artists:',self.artists)
        print('Album:',self.album)
        print('Duration:',self.duration)
        print("-------------")

song1 = Song(
    tracks = 'Song1',
    artists = 'john jennie',
    album='Album2',
    duration = 6.2
)

song2 = Song(
    tracks = 'Song2',
    artists = 'rahul',
    album='Album3',
    duration = 4.5
)

song3 = Song(
    tracks = 'Song3',
    artists = 'george ben',
    album='Album2',
    duration = 5.2
)

#Linking of Objects with Each Other in next and previous form
#Hard Code
song1.next = song2
song2.next = song3
song3.next = song1

song1.previous = song3
song2.previous = song1
song3.previous = song2

song1.show()
song2.show()
song3.show()