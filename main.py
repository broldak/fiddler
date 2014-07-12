from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True


videos = UploadSet('videos', MOVIES)



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


@app.route('/event/<int:event_id>')
def show_event(event_id):
	#event_id will be an integer
	video = Video.load(event_id)
	if video is None:
		abort(404)
	url = videos.url(video.filename)
    """Show an event instance."""
    return render_template('event.html', url = url, photo = photo)

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
