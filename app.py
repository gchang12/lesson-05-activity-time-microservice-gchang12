"""
Prints epoch-time as a string, and displays
it on the Flask application.
"""
from time import time as get_epoch_time

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    Prints epoch-time on home-page.
    """
    return str(get_epoch_time())
