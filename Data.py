

class Video(ndb.Model):
    title = ndb.StringProperty()
    owner = ndb.StringProperty()
    event = ndb.ReferenceProperty(Event)
    location = ndb.GeoPtProperty()
    offset = ndb.FloatProperty()
    timestamp = ndb.DateTimeProperty()

class Event(ndb.Model):
    title = ndb.StringProperty()
    owner = ndb.StringProperty()
    videos = ndb.ListProperty()
    primary = ndb.ReferenceProperty(Video)
    date = ndb.DateProperty()
