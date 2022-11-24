from init_app import db
from src.models.authors_md import Authors
from src.models.books_md import Books
from src.models.authors_books_md import Books_Authors
from src.services.ratings_sv import get_book_ratings_by_stars
from src.utils import is_similar
from src.const import *


def search_by_name(query):
    all_books = Books.query.all()
    result = []
    for book in all_books:
        if is_similar(book.author_name, query):
            result.append(book.get_summary_json())
    if len(result) == 0:
        return None, NOT_FOUND
    return result, OK_STATUS


def search_by_author(query):
    books_authors = Books_Authors.query.all()
    result = []

    for books_author in books_authors:
        author = Authors.query.get(books_author.author_id)
        if is_similar(author.author_name, query):
            book = Books.query.get(books_author.book_id)
            result.append(book.get_summary_json())

    if len(result) == 0:
        return None, NOT_FOUND
    return result, OK_STATUS


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
