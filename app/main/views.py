"""
views.py

url routing to '/', 'login'
"""

from flask import render_template, session, redirect, url_for, abort, current_app, flash, request
from . import main #import blueprint from main/
from datetime import datetime
from flask_moment import Moment

@main.route('/')
def index():
    return render_template('index.html',
                            time=datetime.utcnow())
