from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'paintings_db'

class Painting:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']     
        self.price = data['price']
        self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO paintings (name, description, price, user_id) VALUES ( %(name)s, %(description)s, %(price)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT paintings.*, users.first_name FROM paintings LEFT JOIN users ON users.id = paintings.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        paintings = []
        for painting in results: 
            paintings.append( cls(painting) )
        return paintings

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT paintings.*, FROM paintings WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE paintings SET name=%(name)s, description = %(description)s, price=%(price)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM paintings WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_painting(painting:dict) -> bool:
        
        is_valid = True 
        if len(painting['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(painting['description']) < 10:
            flash("Description must be at least 10 characters.")
            is_valid = False
        if (painting['price']) <= 0:
            flash("price must be greater than 0.")
            is_valid = False     
        return is_valid