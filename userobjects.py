# userobjects.py

class user:
    def __init__(self, username=None, tvShowsList=[]):
        self.username = username
        self.tvShowsList = tvShowsList

class tvShow:
    def __init__(self, tvShowName=None, haveWatched=False, genre=None, seasons=[]):
        self.tvShowName = tvShowName
        self.haveWatched = haveWatched
        self.genre = genre
        self.seasons = seasons

class season:
    def __init__(self, episodes=[]):
        self.episodes = episodes

class episode:
    def __init__(self, Title=None, Index=None, Time=None):
        self.Title=Title
        self.Index=Index
        self.Time=Time
