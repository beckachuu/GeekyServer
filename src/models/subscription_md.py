from init_app import db
from src.utils import is_valid_id, is_valid_username


class Subscription(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))

    def __init__(self, author_name,  username):
        self.author_name = author_name
        self.username = username

    # def get_json(self):
    #     return {
    #         'author_id': self.author_id,
    #         'username': self.username,
    #     }

    def update_author_id(self, new_author_id):
        if self.author_id != new_author_id and is_valid_id(new_author_id):
            self.author_id = new_author_id
            return True
        return False

    def update_username(self, new_username):
        if self.username != new_username and is_valid_username(new_username):
            self.username = new_username
            return True
        return False
