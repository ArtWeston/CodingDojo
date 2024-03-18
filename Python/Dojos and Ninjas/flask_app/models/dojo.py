from ..config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos = []
        results = connectToMySQL('Dojos_Ninjas').query_db(query)
        for row in results:
            dojos.append(cls(row))
        return dojos
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s;"
        return connectToMySQL('Dojos_Ninjas').query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN favorites ON dojos.id = favorites.dojo_id LEFT JOIN ninjas ON ninjas.id = favorites.ninja_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('Dojos_Ninjas').query_db(query,data)

        dojo = cls(results[0])

        for row in results:
            if row['ninjas.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            dojo.ninjas_who_favorited.append(ninja.Ninja(data))
        return dojo

    @classmethod
    def unfavorited_dojos(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id NOT IN ( SELECT dojo_id FROM favorites WHERE ninja_id = %(id)s );"
        results = connectToMySQL('Dojos_Ninjas').query_db(query,data)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        print(dojos)
        return dojos