import sqlalchemy as sql

from init_app import f_sql
from src.controller.auth import login_required


@login_required()
class ReadingService:

    def get_book_content():
        pass

    def edit_theme_preference():
        pass

    def add_bookmark():
        pass

    def add_note():
        pass

    def add_to_collection():
        pass
