import json

from flask import request
from flask_restful import Resource

from config.config import RECOMMEND_PATH
from src.const import *
from src.controller.auth import admin_only, login_required
from src.services.books_sv import *
from src.services.collections_sv import add_book_to_collection


class MainPage(Resource):
    def get(self):
        result = {}
        popular_status = update_popular_books()
        new_book_status = update_new_books()
        personal_list, personal_status = update_personal_recommendation()
        if popular_status != OK_STATUS or new_book_status != OK_STATUS:
            return {MESSAGE: "Our server got an error..."}, SERVER_ERROR


        try:
            with open(RECOMMEND_PATH, 'r') as file:
                recommend = json.load(file)
            result.update(recommend)
            if personal_status == OK_STATUS:
                result.update({"for_this_user":personal_list})
            return result, OK_STATUS
        except:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class BooksSearch(Resource):
    def get(self):
        query_string = request.args.get(QUERY)

        result_by_name, status1 = search_by_name(query_string)
        result_by_author, status2 = search_by_author(query_string)

        if status1 == OK_STATUS or status2 == OK_STATUS:
            return result_by_name + result_by_author, OK_STATUS
        elif status1 == NOT_FOUND and status2 == NOT_FOUND:
            return {MESSAGE: "No book found"}, NOT_FOUND
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class BookDetail(Resource):
    def get(self):
        book_id = request.args.get(BOOK_ID)

        result, status = get_detail_info(book_id)

        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "No book found"}, NOT_FOUND
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def patch(self):
        coll_name = request.args.get("coll_name")
        book_id = request.args.get(BOOK_ID)

        status = add_book_to_collection(coll_name, book_id)
        if status == OK_STATUS:
            return {MESSAGE: "Yay, book is added to your collection!"}, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "No book or collection found"}, NOT_FOUND
        elif status == BAD_REQUEST:
            return {MESSAGE: "Please provide valid info for the request"}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @admin_only()
    def post(self):
        book_info = request.get_json()
        result, status = add_book(book_info)

        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == BAD_REQUEST:
            return {MESSAGE: "Please provide valid info for the book"}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @admin_only()
    def put(self):
        book_info = request.get_json()
        result, status = edit_book_info(book_info)

        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == BAD_REQUEST:
            return {MESSAGE: "Book info isn't changed, please make sure that you provided new and valid info for the book."}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @admin_only()
    def delete(self):
        book_id = request.args.get(BOOK_ID)
        status = remove_book(book_id)
        if status == OK_STATUS:
            return {MESSAGE: "Book is removed."}, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "Can't remove the book you provided (it doesn't exists)"}, NOT_FOUND
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS
