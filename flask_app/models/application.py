from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'Job_Tracker_Schema'

class Application:
    def __init__(self, data):
        self.id = data['id']
        self.position = data['position']
        self.location = data['location']
        self.status = data['status']
        self.comments = data['comments']
        self.link = data['link']
        self.likedin_follow = data['linkedin_follow']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_application(cls, data):
        query = "INSERT INTO applications (position, location, status, comments, link, linkedin_follow, user_id, company_id) VALUES (%(position)s, %(location)s, %(status)s, %(comments)s, %(link)s, %(linkedin_follow)s, %(user_id)s, %(company_id)s)"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_applications(cls):
        query = "SELECT * FROM applications"
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_single_application(cls, data):
        query = "SELECT * FROM applications WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def updated_application(cls, data):
        query = "UPDATE applications SET position=%(position)s, location=%(location)s, status=%(status)s, comments=%(comments)s, link=%(link)s, linkedin_follow=%(linkedin_follow)s WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_application(cls, data):
        query = "DELETE FROM applications WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_application(application):
        is_valid = True
        if len(application['position']) < 3:
            flash("Position Title must be at least 3 characters long")
            is_valid = False
        if len(application['location']) < 2:
            flash("Location must be selected")
            is_valid = False
        return is_valid