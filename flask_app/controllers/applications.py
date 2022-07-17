from flask_app import app
from flask_app.models.application import Application
from flask import render_template, redirect, request, session, flash

@app.route('/applications')
def application_page():
    #pass in session of filter that is being requested.
    return render_template('application_view.html')