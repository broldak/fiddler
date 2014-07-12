from Data import Video

def addVideo(vidFile):
        vid = Video()
        vid.title="test"
        vid.primary = True
        vid.offset = 0
        vid.put()
