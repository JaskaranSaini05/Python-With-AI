class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self,song):
        if self.head == None:
            self.head = song
            self.tail = song
            self.size += 1
        else:
            pass
        