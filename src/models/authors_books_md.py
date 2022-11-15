from init_app import db


class Books_Authors(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, author_id,  book_id):
        self.author_id = author_id
        self.book_id = book_id
