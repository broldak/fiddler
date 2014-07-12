from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import sqlite3

UPLOAD_FOLDER = './videos/'

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/user/<username>')
def show_user(username):
    """Show a user account instance."""
    return render_template('user.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_test():
    if (request.method == 'POST'):
        file = request.files['videofile']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "uploaded"
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

app.run()
