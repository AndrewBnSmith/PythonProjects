from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'login'

class Model:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO models (param1, param2, user_id, param3) VALUES ( %(param1)s, %(param2)s, %(user_id)s, %(param3)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        models = []
        for model in results: 
            models.append( cls(model) )
        return models

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE users SET param1=%(param1)s, param2=%(param2)s, user_id=%(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_model(model:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(model['param1']) < 5:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(model['param2']) < 2:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid