"""Main Flask app."""

from flask import Flask

# Calling this "application" makes it easier for gunicorn to find
application = Flask(__name__)

# TODO: Make content type JSON.
# TODO: Implement other endpoints.
@application.route('/')
def index():
    return '''
    {
        "doc": "Create a risk type with /risk endpoint.\nGet a risk by id with /risks endpoint."
        "endpoints": [
            "/risk",
            "/risks",
        ]
    }
    '''
