from flask import request
from flask_restful import Resource

from src.const import *
from src.controller.auth import get_current_user
from src.services.books_sv import *


class MainPage(Resource):
    def get(self):
        user = get_current_user()
        result = get_general_recommendation()
        if user is not None:
            result += get_general_recommendation(user)
        return result, OK_STATUS


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
    def get(self):
        book_id = request.args.get(BOOK_ID)

        result, status = get_detail_info(book_id)

        if status == OK_STATUS:
            return result, OK_STATUS
        return {MESSAGE: "No book found"}, NOT_FOUND

    @admin_only()
    def post(self):
        book_info = request.get_json()
        result, status = add_book(book_info)

        if status == OK_STATUS:
            return result, OK_STATUS
        else:
            return {MESSAGE: "Please provide valid info for the book"}, BAD_REQUEST

    @admin_only()
    def put(self):
        pass
