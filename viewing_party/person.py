class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.watchlist = []
        self.watched = []


    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


    def watch(self, movie):
        if movie in self.watchlist:
            self.watchlist.remove(movie)
        
        if movie not in self.watched:
            self.watched.append(movie)


    def add_to_watchlist(self, movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)
    