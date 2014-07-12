from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True

from google.appengine.api import files

@app.route('/user/<username>')
def show_user(username):
    """Show a user account instance."""
    return render_template('user.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if (request.method == 'POST'):
        data_file = request.files.get('file')
        filename = VideoManager.addfile(data_file, request.args.get('title'))
        print filename
    return render_template('upload.html')

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
