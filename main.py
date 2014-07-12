from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

import VideoManager


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    VideoManager.addVideo("tt")
    return render_template('layout.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
