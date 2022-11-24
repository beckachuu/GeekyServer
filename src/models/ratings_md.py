from init_app import db
from src.const import *


class Ratings(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    book_id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)
    content = db.Column(db.String)

    def __init__(self, username, book_id, stars, content):
        self.username = username
        self.book_id = book_id
        self.stars = stars
        self.content = content

    def get_json(self):
        return {
            'username': self.username,
            'book_id': self.book_id,
            'stars': self.stars,
            'content': self.content,
        }

    def update_stars(self, new_stars):
        if new_stars.isnumeric() and self.stars != new_stars and new_stars >= 1 and new_stars <= 5:
            return True
        return False

    def update_content(self, new_content):
        if self.content != new_content:
            self.content = new_content
            return True
        return False
