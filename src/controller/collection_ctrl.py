from flask import request
from flask_restful import Resource

from src.const import *
from src.controller.auth import login_required
from src.services.collections_sv import *


class MyCollections(Resource):
    @login_required()
    def post(self, coll_name):
        result, status = create_collection(coll_name)

        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == BAD_REQUEST:
            return {MESSAGE: "Your collection name is invalid"}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def patch(self, coll_name):
        new_name = request.args.get("new_name")
        status = edit_collection_name(coll_name, new_name)

        if status == OK_STATUS:
            return {MESSAGE: "{old_name}'s name is noew {new_name}".format(coll_name, new_name)}, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "Can't find your collection"}, NOT_FOUND
        elif status == BAD_REQUEST:
            return {MESSAGE: "Please provide valid name for you collection"}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def put(self, coll_name):
        book_id = request.args.get(BOOK_ID)
        status = remove_book_from_collection(coll_name, book_id)

        if status == OK_STATUS:
            return {MESSAGE: "Book is removed from your collection"}, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "Can't find your collection"}, NOT_FOUND
        elif status == BAD_REQUEST:
            return {MESSAGE: "The collection name is invalid"}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def delete(self, coll_name):
        result, status = delete_collection(coll_name)

        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "Can't find your collection"}, NOT_FOUND
        elif status == BAD_REQUEST:
            return {MESSAGE: "The collection name is invalid"}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS
