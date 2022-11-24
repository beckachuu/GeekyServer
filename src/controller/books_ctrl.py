from flask import request
from flask_restful import Resource

from src.const import *
from src.controller.auth import login_required
from src.services.books_sv import *


class MainPage(Resource):
    # TODO: return recommendation (and recent interacted books, via rating/subscription...)
    def get(self):
        return {MESSAGE: "You're at our main page"}


class BooksSearch(Resource):
    def get(self):
        query_string = request.args.get(QUERY)
        result_by_name, status1 = search_by_name(query_string)
        result_by_author, status2 = search_by_author(query_string)

        if status1 == OK_STATUS or status2 == OK_STATUS:
            return result_by_name+result_by_author, OK_STATUS
        else:
            return {MESSAGE: "No book found"}, NOT_FOUND


class BookDetail(Resource):
    def get(self, book_id):
        result = request.get_json()
        return {MESSAGE: result['book']}


class Recommendation(Resource):
    def get(self):
        book_list = []
        return book_list

    @login_required()
    def post(self):
        # Send user's activity to update recommendation
        return {MESSAGE: "suceeded"}
