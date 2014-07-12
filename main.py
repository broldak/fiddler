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

UPLOAD_FOLDER = './videos/'
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/user/<username>')
def show_user(username):
    """Show a user account instance."""
    return render_template('user.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if (request.method == 'POST'):
        file = request.files['videofile']
        print (not file)
        if file:
            tmeStamp=getTimestamp(request.form['lmd'])
            vid = Video(title=file.filename, timestamp=tmeStamp, offset=getOffset(tmeStamp, "axtdkwnOn8") )
            vid.save()
            filename = vid.objectId
            print filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print os.path.join(app.config['UPLOAD_FOLDER'], filename)
            return "uploaded"
    return render_template('upload.html')

@app.route('/createEvent', methods=['GET'])
def createEvent():
    evnt = Event(title=request.args['title'], primary="")
    evnt.save()
    return show_event(evnt.objectId)

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

@app.route('/event/<int:event_id>')
def show_event(event_id):
  #video = Video.load(event_id)
  #if video is None:
  #  abort(404);
  #url = videos.url(video.filename)
  return render_template('event.html')

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
