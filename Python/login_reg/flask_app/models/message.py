from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
from flask_app.models import user
import math

class Message:
    DB = 'private_wall'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.content = db_data['content']
        self.sender = db_data['sender']
        self.reciever = db_data['receiver']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_user_messages(cls,user_id):

        receiver = user.User.get_by_id(user_id)

        query = """SELECT messages.*,
                first_name, last_name, email, senders.created_at as sender_created_at, senders.updated_at as sender_updated_at
                FROM messages
                JOIN users as senders on messages.sender_id = senders.id
                WHERE receiver_id =  %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query,{"id": user_id})

        messages = []

        for message in results:
            sender_data = {
                "id": message["sender_id"],
                "first_name": message["first_name"],
                "last_name": message["last_name"],
                "email": message["email"],
                "created_at": message["sender_created_at"],
                "updated_at": message["sender_updated_at"],
            }
            sender = user.User(sender_data)

            message = {
                "id": message["id"],
                "content": message["content"],
                "sender": sender,
                "receiver": receiver,
                "created_at": message["created_at"],
                "updated_at": message["updated_at"],
            }
            messages.append( cls(message) )

        return messages

    @classmethod
    def save(cls,data):
        query = "INSERT INTO messages (content,sender_id,receiver_id) VALUES (%(content)s,%(sender_id)s,%(receiver_id)s);"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def destroy(cls, message_id):
        query = "DELETE FROM messages WHERE messages.id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,{"id": message_id})

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"