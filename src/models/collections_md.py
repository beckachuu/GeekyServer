from init_app import db
from src.controller.auth import get_current_user
from src.models.books_md import Books
from src.utils import *


class Collections(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    coll_name = db.Column(db.String(50), primary_key=True)
    book_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, username):
        self.username = username
        self.coll_name = None
        self.book_id = None

    @staticmethod
    def get_json(username, coll_name):
        '''
        Get JSON of a collection by the owner's username and its name
        '''
        collections_query = Collections.query.filter_by(
            username=username, coll_name=coll_name)
        book_ids = []
        for collection in collections_query:
            book_ids.append(collection.book_id)

        return {
            'username': username,
            'coll_name': coll_name,
            'book_ids': book_ids,
        }

    @staticmethod
    def update_coll_name(coll_name, new_coll_name):
        user = get_current_user()
        if is_valid_name(new_coll_name, COLL_NAME_MAX_LENGTH):

            collections = Collections.query.filter_by(
                username=user.username, coll_name=coll_name)
            if collections.first().coll_name == new_coll_name:
                return False

            for collection in collections:
                collection.coll_name = new_coll_name
            return True

        return False
