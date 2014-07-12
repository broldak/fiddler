class Video(ndb.Model):
    title = nbd.StringProperty()
    name = ndb.StringProperty()
    location = ndb.IntegerProperty()
    primary = ndb.BooleanProperty()
