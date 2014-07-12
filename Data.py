from google.appengine.api import users
from google.appengine.ext import ndb

class Video(ndb.Model):
    title = ndb.StringProperty()
    owner = ndb.StringProperty()
    name = ndb.StringProperty()
    location = ndb.GeoPtProperty()
    offset = ndb.IntegerProperty()
    primary = ndb.BooleanProperty()
    create_date = ndb.DateTimeProperty()
