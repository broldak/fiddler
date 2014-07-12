from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import VideoManager
import os, time
import settings_local
from parse_rest.datatypes import Object
from parse_rest.connection import register
register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY)

class Video(Object):
    pass

class Event(Object):
    pass

UPLOAD_FOLDER = './static/vid/'
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/user/<username>')
def show_user(username):
    """Show a user account instance."""
    return render_template('user.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    eventId = request.args['event']
    if (request.method == 'POST'):
        file = request.files['videofile']
        print (not file)
        if file:
            tmeStamp=getTimestamp(request.form['lmd'])
            vid = Video(title=file.filename, timestamp=tmeStamp, event=eventId, offset=getOffset(tmeStamp, eventId) )
            vid.save()
            if vid.offset == 0:
                evnt = Event.Query.get(objectId=eventId)
                evnt.primary = vid.objectId
                evnt.save()
            filename = vid.objectId
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return show_event(eventId)
    return render_template('upload.html', eventId=eventId)

@app.route('/createEvent', methods=['GET'])
def createEvent():
    evnt = Event(title=request.args['title'], primary="")
    evnt.save()
    return redirect('/event/'+evnt.objectId)

def getTimestamp(strTime):
    print strTime
    tym = strTime.split(" ")
    ret = ""
    for i in tym[0:5]:
        ret = ret +  i +" "
    return ret

def getOffset(vidTime, eventId):
    p = "%a %b %d %Y %H:%M:%S "
    dattme_video = time.strptime(vidTime, p)
    evnt = Event.Query.get(objectId=eventId)
    if( not evnt.primary):
        return 0
    else:
        prim = Video.Query.get(objectId=evnt.primary)
        dattme_event = time.strptime(prim.timestamp, p)
        return (time.mktime(dattme_video) - time.mktime(dattme_event))

@app.route('/event/<event_id>')
def show_event(event_id):
  evt = Event.Query.get(objectId=event_id)
  videos = sortVideos(Video.Query.filter(event=event_id))

  return render_template('event.html', evt = evt, video_list=videos)

def sortVideos(videos):
  video_list = []
  for i in videos:
    video_list.append(i)

  if(len(video_list)<1):
    return video_list  

  for i in range(0, len(video_list)):
    for j in range(0, len(video_list)):
      if(video_list[i].offset > video_list[j].offset):
        temp = video_list[i]
        video_list[i] = video_list[j]
        video_list[j] = temp
  video_list.reverse()

  minOffset = video_list[0].offset
  if(minOffset < 0 ):
    for i in video_list:
      i.offset = abs(minOffset) + i.offset
      i.save()

  return video_list

@app.route('/')
def home():
    """Default Home Page."""
    return render_template('home.html')

@app.route('/test')
def test():
    """Test (for testing purposes."""
    return "Test"

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

app.run()
