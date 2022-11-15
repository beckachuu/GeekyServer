from init_app import db
from src.models.authors_books_md import Books_Authors
from src.models.ratings_md import Ratings


class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    translator = db.Column(db.String(70))
    cover = db.Column(db.String)
    genre = db.Column(db.String(40))
    page_count = db.Column(db.Integer)
    public_year = db.Column(db.Integer)
    content = db.Column(db.String)
    descript = db.Column(db.String)
    republish_count = db.Column(db.Integer)
    current_rating = db.Column(db.Float)

    authors = []

    def __init__(self, title, genre, page_count, public_year, content, descript, translator=None, cover=None, republish_count=None, current_rating=None):
        self.title = title
        self.translator = translator
        self.cover = cover
        self.genre = genre
        self.page_count = page_count
        self.public_year = public_year
        self.content = content
        self.descript = descript
        self.republish_count = republish_count
        self.current_rating = current_rating

        authors_query = Books_Authors.query.filter_by(book_id=self.book_id)
        authors = {}
        for author in authors_query:
            authors[author.author_id] = author.author_name

    def get_summary_json(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'authors': self.authors,
            'current_rating': self.current_rating,
            'genre': self.genre,
        }

    def get_detail_json(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'authors': self.authors,
            'genre': self.genre,
            'translator': self.translator,
            'page_count': self.page_count,
            'public_year': self.public_year,
            'republish_count': self.republish_count,
            'descript': self.descript,
        }
