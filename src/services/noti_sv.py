from datetime import datetime

from init_app import db
from src.models.authors_md import Authors
from src.models.books_md import Books
from src.models.collections_md import Collections
from src.models.noti_md import Notifications
from src.models.subscription_md import Subscription

BOOK_UPDATE_NOTI = "{bookname} has some new updates!"
AUTHOR_NEW_BOOK_NOTI = "{author_name} has a new work!"
BOOK_DETAIL_PATH = "/books?book_id={id}"


def notify_book_update(book_id):
    book = Books.query.filter_by(book_id=book_id).first()
    usernames = Collections.query(
        Collections.username.distinct()).filter_by(book_id=book_id)
    for username in usernames:
        new_noti = Notifications(username, BOOK_UPDATE_NOTI.format(
            book.title), datetime.today(), BOOK_DETAIL_PATH.format(book_id))
        db.session.add(new_noti)
    db.session.commit()


def notify_authors_new_book(author_ids, book_id):
    for author_id in author_ids:
        author = Authors.query.filter_by(author_id=author_id).first()
        usernames = Subscription.query(
            Subscription.username.distinct()).filter_by(author_id=author_id)
        for username in usernames:
            new_noti = Notifications(username, AUTHOR_NEW_BOOK_NOTI.format(
                author.author_name), datetime.today(), BOOK_DETAIL_PATH.format(book_id))
            db.session.add(new_noti)
    db.session.commit()
