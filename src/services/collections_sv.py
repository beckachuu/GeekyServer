from init_app import db
from src.const import *
from src.models.authors_books_md import BooksAuthors
from src.models.authors_md import Authors
from src.models.books_md import Books
from src.services.ratings_sv import get_ratings_by_stars
from src.utils import is_similar
from src.controller.auth import login_required


@login_required()
def create_collection(coll_name):
    pass


@login_required()
def get_collection_details():
    pass


@login_required()
def edit_collection_name(new_name):
    pass


@login_required()
def remove_book_from_collection(coll_name, book_id):
    pass
