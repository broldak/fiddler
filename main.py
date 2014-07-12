from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

import VideoManager


<<<<<<< HEAD
@app.route('/event/<int:event_id>')
def show_event(event_id):
	#event_id will be an integer
    """Show an event instance."""
    return render_template('event.html')
=======
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    VideoManager.addVideo("tt")
    return render_template('layout.html')
>>>>>>> 8503bf0c727d0858418d707a0e2442dbef45fabb

@app.route('/user/<username>')
def show_user(username):
    """Show a user account instance."""
    return render_template('user.html')

@app.route('/upload')
def upload():
    """Show the page to allow a video upload."""
    return render_template('upload.html')

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
