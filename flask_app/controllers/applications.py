from email.policy import default
from flask_app import app
from flask_app.models.application import Application
from flask import render_template, redirect, request, session, flash

@app.route('/application/new')
def create_application():
    return render_template('application_create.html')

@app.route('/application/create', methods=['POST'])
def add_application():
    data = {
        "position": request.form['position'],
        "location": request.form['location'],
        "status": request.form['status'],
        "comments": request.form['comments'],
        "link": request.form['link'],
        "linkedin_follow": request.form['linkedin_follow'],
        "user_id": request.form['user_id'],
        "company_id": request.form['company_id']
    }
    Application.add_application(data)
    return redirect('/dashboard')

@app.route('/application/edit')
def edit_application():
    return render_template('application_update.html')

@app.route('/application/update')
def update_application():
    data = {
        "position": request.form['position'],
        "location": request.form['location'],
        "status": request.form['status'],
        "comments": request.form['comments'],
        "link": request.form['link'],
        "linkedin_follow": request.form['linkedin_follow'],
        "user_id": request.form['user_id'],
        "company_id": request.form['company_id']
    }
    Application.updated_application(data)
    return redirect('/dashboard')

@app.route('/application/<int:id>')
def single_application_page(id):
    #pass in data - application: id
    application = Application.get_single_application(id)
    return render_template('applicaion_read.html', single_application = application)

@app.route('/application', defaults={'status': 'Applied'})
@app.route('/application/<status>')
def status_page():
    #pass in data - applications status

    return render_template('status_page.html')

#Perhaps we can remove all this and instead have a variable in the url for the status we want to pull up.
# @app.route('/application/status/interview_scheduled')
# def status_page():
#     #pass in data - applications status: interview_scheduled
#     return render_template('status_page.html')

# @app.route('/application/status/signed')
# def status_page():
#     #pass in data - applications status: signed
#     return render_template('status_page.html')

# @app.route('/application/status/archived')
# def status_page():
#     #pass in data - applications status: archived
#     return render_template('status_page.html')

# @app.route('/application/status/expired')
# def status_page():
#     #pass in data - applications status: expired
#     return render_template('status_page.html')