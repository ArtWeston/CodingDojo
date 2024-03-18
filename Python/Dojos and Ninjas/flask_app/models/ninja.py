from ..config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas = []
        results = connectToMySQL('Dojos_Ninjas').query_db(query)
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age) VALUES (%(first_name)s, %(last_name)s, %(age)s);"
        return connectToMySQL('Dojos_Ninjas').query_db(query,data)

    @classmethod
    def unfavorited_ninjas(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id NOT IN ( SELECT ninja_id FROM favorites WHERE dojo_id = %(id)s );"
        ninjas = []
        results = connectToMySQL('Dojos_Ninjas').query_db(query,data)
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('Dojos_Ninjas').query_db(query,data);


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('Dojos_Ninjas').query_db(query,data)

        # Creates instance of author object from row one
        ninja = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['dojos.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['dojos.id'],
                "name": row['name'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['dojos.created_at'],
                "updated_at": row['dojos.updated_at']
            }
            ninja.favorite_ninjas.append(ninja.Book(data))
        return ninja