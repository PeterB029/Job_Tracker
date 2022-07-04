from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'Job_Tracker_Schema'

class Company:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_company(cls, data):
        query = "SELECT * FROM companies WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_application(application):
        is_valid = True
        if len(application['name']) < 3:
            flash("Company name must be at least 3 characters long")
            is_valid = False
        return is_valid