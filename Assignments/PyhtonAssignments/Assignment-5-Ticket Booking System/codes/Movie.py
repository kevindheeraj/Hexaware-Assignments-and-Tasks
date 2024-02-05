from bean.Events import Event

class Movie(Event):
    def __init__(self, event, genre, actorName, actressName):
        self.event = event
        self.genre = genre
        self.actorName = actorName
        self.actressName = actressName

    @property
    def getname(self):
        return self.event.event_name

    @getname.setter
    def setname(self, name):
        self.event.event_name = name

