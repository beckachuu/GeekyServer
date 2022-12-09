from init_app import db
from src.const import *
from src.models.bookmarks_md import Bookmark
from src.controller.auth import get_current_user

BOOKMARK_NAME = 'bm_name'
LINE_POS = 'line_pos'


def get_bookmark(book_id, bm_name):
    user = get_current_user()
    bookmark = Bookmark.query.filter_by(
        username=user.username, book_id=book_id, bm_name=bm_name).first()

    if bookmark:
        return bookmark.get_json(), OK_STATUS
    return None, NOT_FOUND


def add_bookmark(json):
    user = get_current_user()
    bookmark = Bookmark(user.username)

    if bookmark.update_book_id(json[BOOK_ID]) and bookmark.update_bm_name(json[BOOKMARK_NAME]):
        bookmark.update_line_pos(json[LINE_POS])
        bookmark.update_content(json[CONTENT])

        try:
            db.session.add(bookmark)
            db.session.commit()
            return OK_STATUS
        except:
            return CONFLICT
    return BAD_REQUEST


def edit_bookmark(json):
    user = get_current_user()
    try:
        bookmark = Bookmark.query.filter_by(
            username=user.username, book_id=json[BOOK_ID], bm_name=json[BOOKMARK_NAME]).first()

        if bookmark.update_bm_name(json[BOOKMARK_NAME]) or bookmark.update_line_pos(json[LINE_POS]) or bookmark.update_content(json[CONTENT]):
            db.session.commit()
            return OK_STATUS
        return NO_CONTENT
    except:
        return BAD_REQUEST


def delete_bookmark(book_id, bm_name):
    user = get_current_user()
    try:
        bookmark = Bookmark.query.filter_by(
            username=user.username, book_id=book_id, bm_name=bm_name).first()

        if not bookmark:
            return NOT_FOUND

        db.session.delete(bookmark)
        db.session.commit()

        return OK_STATUS
    except:
        return BAD_REQUEST
