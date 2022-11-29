from init_app import db
from src.const import *
from src.controller.auth import get_current_user
from src.models.books_md import Books
from src.models.collections_md import Collections
from src.utils import is_valid_name


def create_collection(coll_name):
    user = get_current_user()
    new_coll = Collections(user.username)
    if is_valid_name(coll_name, COLL_NAME_MAX_LENGTH):
        new_coll.coll_name = coll_name
        db.session.add(new_coll)
        db.session.commit()
        return new_coll.get_json(), OK_STATUS
    return None, BAD_REQUEST


def edit_collection_name(coll_name, new_name):
    user = get_current_user()
    try:
        collections = Collections.query.filter_by(
            username=user.username, coll_name=coll_name)
        if collections and Collections.update_coll_name(user.username, coll_name, new_name):
            for collection in collections:
                collection.coll_name = coll_name
            db.session.commit()
            return OK_STATUS
        return NOT_FOUND
    except:
        return BAD_REQUEST


def remove_book_from_collection(coll_name, book_id):
    user = get_current_user()
    try:
        collection = Collections.query.filter_by(
            username=user.username, coll_name=coll_name, book_id=book_id).first()
        if collection:
            db.session.delete(collection)
            db.session.commit()
            return OK_STATUS
        return NOT_FOUND
    except:
        return BAD_REQUEST


def delete_collection(coll_name):
    user = get_current_user()
    try:
        collections = Collections.query.filter_by(
            username=user.username, coll_name=coll_name)
        if collections:
            for collection in collections:
                db.session.delete(collection)
            db.session.commit()
            return OK_STATUS
        return NOT_FOUND
    except:
        return BAD_REQUEST


def add_book_to_collection(coll_name, book_id):
    user = get_current_user()
    try:
        book = Books.query.get(book_id)
        collections = Collections.query.filter_by(
            username=user.username, coll_name=coll_name)
        if book and collections:
            for collection in collections:
                collection.book_id = book_id
            db.session.commit()
            return OK_STATUS
        return NOT_FOUND
    except:
        return BAD_REQUEST
