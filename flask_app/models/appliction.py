from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

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
        pass

    @classmethod
    def get_application(cls, data):
        pass

    @classmethod
    def updated_application(cls, data):
        pass

    @classmethod
    def delete_application(cls, data):
        pass

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