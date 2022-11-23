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

    def update_quote(self, new_quote):
        if self.quote != new_quote:
            self.quote = new_quote
            return True
        return False
