from init_app import db
from src.models.books_md import Books


class Collections(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    coll_name = db.Column(db.String(50), primary_key=True)

    def __init__(self, username, coll_name):
        self.username = username
        self.coll_name = coll_name

    def get_json(self):
        books = Books.query.filter_by(username=self.username)
        book_ids = []
        for book in books:
            book_ids.append(book.book_id)

        return {
            'username': self.username,
            'coll_name': self.coll_name,
            'book_ids': book_ids,
        }
