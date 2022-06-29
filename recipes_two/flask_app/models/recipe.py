from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'recipes_db'

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
       
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO recipes (name, description, instructions, under_thirty, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(under_thirty)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for recipe in results: 
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE recipes SET name=%(name)s, description = %(description)s, instructions=%(instructions)s, under_thirty=%(under_thirty)s, user_id=%(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True 
        if len(recipe['name']) < 5:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(recipe['instructions']) < 2:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid


    
