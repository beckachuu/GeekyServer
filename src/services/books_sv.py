import sqlalchemy as sql

from init_app import db
from src.models.books_md import Books
from src.services.ratings_sv import get_book_ratings_by_stars


def search_by_bookname():
    pass


def search_by_author():
    pass


def get_summary_info(book_id):
    book = Books.query.filter_by(book_id=book_id).first()
    return book.get_detail_json()


def get_detail_info(book_id):
    book = Books.query.filter_by(book_id=book_id).first()
    return book.get_detail_json() + {
        'one_stars': get_book_ratings_by_stars(book_id, 1),
        'two_stars': get_book_ratings_by_stars(book_id, 2),
        'three_stars': get_book_ratings_by_stars(book_id, 3),
        'four_stars': get_book_ratings_by_stars(book_id, 4),
        'five_stars': get_book_ratings_by_stars(book_id, 5),
    }

# general: by ratings + reports (of the books)
# personal: by rating + report activities


def recommendation():
    pass


def get_sharable_links():
    pass
