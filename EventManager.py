from data import Event, Video
import VideoManager

def addEvent(event, title):
    ev = Event()
    ev.title = titles
    ev.primary = ""

def addVideo(event, videoId):
    event.videos = event.videos.append(videoId)
    VideoManager.setEvent(videoId, event)
