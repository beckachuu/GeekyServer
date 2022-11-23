from init_app import db
from src.utils import is_valid_name
from src.const import GENRE_MAX_LENGTH


class Genres(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String, primary_key=True)

    def __init__(self, book_id, genre):
        self.book_id = book_id
        self.genre = genre

    @staticmethod
    def update_genre(book_id, new_genres):
        if isinstance(new_genres, list):
            return False

        for genre in new_genres:
            if not is_valid_name(genre, GENRE_MAX_LENGTH):
                return False

        book_genres_query = Genres.query.filter_by(book_id=book_id)
        for book in book_genres_query:
            for genre in new_genres:
                book.genre = genre
        return True
