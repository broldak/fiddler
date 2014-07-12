from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True

from google.appengine.api import files

#videos = UploadSet('videos', MOVIES)

@app.route('/user/<username>')
def show_user(username):
    """Show a user account instance."""
    return render_template('user.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if (request.method == 'POST' and 'video' in request.files):
        filename = videos.save(request.files[video])
        rec = Video(filename=filename, user=g.user.id)
        rec.store()
        flash("Video saved.")
        return redirect(url_for('show', id=rec.id))
    return render_template('upload.html')

@app.route('/testwrite')
def uploadVideo(file, title):
    filename = "/gs/fiddlerhack.appspot.com/videos/" + VideoManager.addVideo(file, title)
    writable_file_name = files.gs.create(filename, mime_type='application/octet-stream', acl='public-read')
    with files.open(writable_file_name, 'a') as f:
        f.write("test")
    files.finalize(writable_file_name)


@app.route('/event/<int:event_id>')
def show_event(event_id):
  video = Video.load(event_id)
  if video is None:
    abort(404);
  url = videos.url(video.filename)
  return render_template('event.html')


@app.route('/home')
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
