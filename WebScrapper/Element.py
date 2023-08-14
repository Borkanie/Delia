from datetime import datetime

class Element:
    name = ""
    date = datetime.now()
    location = ""
    def __init__(self,name,date,location):
        self.name = name
        self.date = date
        self.location =location

    def JSON(self):
        return {
            'name': self.name,
            'date': self.date,
            'location' : self.location
        }