from init_app import db
from src.utils import is_valid_id


class BooksAuthors(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, primary_key=True)

    def __init__(self):
        self.author_id = None
        self.book_id = None
