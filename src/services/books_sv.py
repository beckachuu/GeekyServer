import sqlalchemy as sql

from init_app import f_sql
from src.controller.auth import admin_only


class BooksService:

    def search_by_bookname():
        pass

    def search_by_author():
        pass

    def get_summary_info():
        pass

    def get_detail_info():
        pass

    # fp-treeee
    # general: by ratings + reports (of the books)
    # personal: by rating + report activities
    def recommendation():
        pass

    def get_sharable_links():
        pass
