from init_app import db
from src.const import *
from src.controller.auth import admin_only, login_required
from src.models.authors_books_md import BooksAuthors
from src.models.authors_md import Authors
from src.models.books_md import Books
from src.models.genres_md import Genres
from src.services.ratings_sv import get_ratings_by_stars
from src.utils import is_similar


def get_general_recommendation(limit=MAX_RESULT_COUNT):
    # TODO
    all_books = Books.query.all()
    result = []
    for book in all_books:
        result.append(book.get_summary_json())
    if len(result) == 0:
        return None, NOT_FOUND
    return result, OK_STATUS


def get_recent_updated(limit=MAX_RESULT_COUNT):
    # TODO
    pass


def get_personal_recommendation(user, limit=MAX_RESULT_COUNT):
    # by user ratings, subscription, bookmarks, collections
    # TODO
    return None


def search_by_name(query):
    all_books = Books.query.all()
    result = list()
    for book in all_books:
        if is_similar(book.title, query):
            result.append(book.get_summary_json())
    if len(result) == 0:
        return [], NOT_FOUND
    return result, OK_STATUS


def search_by_author(query):
    books_authors = BooksAuthors.query.all()
    result = list()

    for books_author in books_authors:
        author = Authors.query.get(books_author.author_id)
        print(author.author_name)
        if is_similar(author.author_name, query):
            book = Books.query.get(books_author.book_id)
            result.append(book.get_summary_json())

    if len(result) == 0:
        return [], NOT_FOUND
    return result, OK_STATUS


def get_detail_info(book_id):
    book = Books.query.filter_by(book_id=book_id).first()
    if book is None:
        return None, NOT_FOUND

    ratings = {}
    for i in range(1, 6):
        ratings.update(get_ratings_by_stars(book_id, i))

    result = book.get_detail_json()
    result.update(ratings)

    return result, OK_STATUS


def add_book(json):
    book = Books()

    if book.is_valid_book(json[TITLE], json[PAGE_COUNT], json[PUBLIC_YEAR], json[CONTENT], json[DESCRIPT]):
        book.update_translator(json[TRANSLATOR])
        book.update_cover(json[COVER])
        book.update_republish_count(json[REPUBLISH_COUNT])

        db.session.add(book)
        db.session.commit()

        Genres.add_genres(book.book_id, json[GENRES])
        BooksAuthors.add_books_authors(book.book_id, json[AUTHORS])

        return book.get_detail_json(), OK_STATUS

    return None, BAD_REQUEST


def edit_book_info(json):
    book = Books.query.filter_by(book_id=json[BOOK_ID]).first()
    updated = False

    if book.update_title(json[TITLE]):
        updated = True
    if book.update_page_count(json[PAGE_COUNT]):
        updated = True
    if book.update_public_year(json[PUBLIC_YEAR]):
        updated = True
    if book.update_content(json[CONTENT]):
        updated = True
    if book.update_descript(json[DESCRIPT]):
        updated = True
    if book.update_translator(json[TRANSLATOR]):
        updated = True
    if book.update_cover(json[COVER]):
        updated = True
    if book.update_republish_count(json[REPUBLISH_COUNT]):
        updated = True
    if Genres.update_genres(book.book_id, json[GENRES]):
        updated = True
    if BooksAuthors.update_books_authors(book.book_id, json[AUTHORS]):
        updated = True

    if updated:
        db.session.commit()
        return book.get_detail_json(), OK_STATUS

    return None, BAD_REQUEST


@ admin_only()
def remove_book():
    pass


@login_required()
def add_to_collection():
    pass


@login_required()
def add_bookmark():
    pass


@login_required()
def add_note():
    pass
