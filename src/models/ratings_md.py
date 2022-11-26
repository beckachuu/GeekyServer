from init_app import db
from src.const import *


class Ratings(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    book_id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)
    content = db.Column(db.String)

    def __init__(self):
        self.username = None
        self.book_id = None
        self.stars = None
        self.content = None

    def get_json(self):
        return {
            'username': self.username,
            'book_id': self.book_id,
            'stars': self.stars,
            'content': self.content,
        }

    def update_stars(self, new_stars):
        if isinstance(new_stars, int) and self.stars != new_stars and new_stars >= 1 and new_stars <= 5:
            return True
        return False

    def update_content(self, new_content):
        if self.content != new_content:
            self.content = new_content
            return True
        return False
