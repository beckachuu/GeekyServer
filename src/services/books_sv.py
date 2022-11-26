from init_app import db
from src.const import *
from src.models.authors_books_md import BooksAuthors
from src.models.authors_md import Authors
from src.models.books_md import Books
from src.services.ratings_sv import get_ratings_by_stars
from src.utils import is_similar
from src.controller.auth import admin_only


def get_general_recommendation(limit=MAX_RESULT_COUNT):
    # TODO
    pass


def get_recent_updated(limit=MAX_RESULT_COUNT):
    # TODO
    pass


def get_personal_recommendation(user, limit=MAX_RESULT_COUNT):
    # by user ratings, subscription, bookmarks, collections
    # TODO
    pass


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
    books_authors = BooksAuthors.query.all()
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
    if book is None:
        return None, NOT_FOUND

    ratings = {}
    for i in range(1, 6):
        ratings.update(get_ratings_by_stars(book_id, i))

    return ratings, OK_STATUS


@admin_only()
def add_book(json):
    book = Books()

    if book.is_valid_book(json[TITLE], json[PAGE_COUNT], json[PUBLIC_YEAR], json[CONTENT], json[DESCRIPT]):
        book.update_translator(json[TRANSLATOR])
        book.update_cover(json[COVER])
        book.update_republish_count(json[REPUBLISH_COUNT])

        db.session.add(book)
        db.session.commit()

        return book.get_json(), OK_STATUS

    return None, BAD_REQUEST


@admin_only()
def edit_book_info():
    pass


@admin_only()
def remove_book():
    pass
