from init_app import db


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
