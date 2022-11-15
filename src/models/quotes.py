from init_app import db


class AuthorsQuotes(db.Model):
    quote_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String)

    def __init__(self,  book_id, author_id, quote):
        self.quote_id = book_id
        self.author_id = author_id
        self.quote = quote

    def get_json(self):
        return {
            'quote_id': self.quote_id,
            'author_id': self.author_id,
            'quote': self.quote,
        }
