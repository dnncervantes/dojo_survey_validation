from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO surveys (name, location, language, comments, created_at) VALUES (%(name)s, %(location)s, %(language)s, %(comments)s, NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @classmethod
    def get_last_survey(cls): 
        query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        # print(results[0])
        # print(cls(results[0]))
        return cls(results[0])

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(survey['comments']) < 2:
            is_valid = False
            flash("Comments must be at least 2 character.")
        return is_valid
        

    # @classmethod
    # def show(cls, data):
    #     query = "SELECT * FROM projectTable WHERE projectTable.id = %(id)s;"
    #     projectTable_from_db = connectToMySQL('projectDB').query_db(query,data)

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE projectTable SET xx=%(xx)s, xx=%(xx)s, updated_at = NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('projectDB').query_db(query,data)

    # @classmethod
    # def delete(cls,data):
    #     query = "DELETE FROM projectTable WHERE id = %(id)s;"
    #     return connectToMySQL('projectDB').query_db(query,data)