from flask import request
from flask_restful import Resource

from src.const import *
from src.controller.auth import login_required
from src.services.ratings_sv import *
from src.services.users_sv import *
from src.services.collections_sv import *


class MyAccount(Resource):
    @login_required()
    def get(self):
        result, status = get_own_account()

        if status == OK_STATUS:
            return result, OK_STATUS
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def post(self):
        new_info = request.get_json()

        username = new_info[USERNAME]
        name = new_info[NAME]
        phone = new_info[PHONE]
        profile_pic = new_info[PROFILE_PIC]
        theme_preference = new_info[THEME]

        status = edit_own_account(username, name, phone,
                                  profile_pic, theme_preference)

        if status == OK_STATUS:
            return {MESSAGE: "Your profile is updated"}, OK_STATUS
        elif status == NO_CONTENT:
            return {MESSAGE: "Your profile is the same. Please recheck your input"}, OK_STATUS
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def delete(self):
        status = remove_own_account()
        if status == OK_STATUS:
            return {MESSAGE: "Your account is deleted."}, OK_STATUS
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class MyNoti(Resource):
    @login_required()
    def get(self):
        result, status = get_my_noti()
        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == NO_CONTENT:
            return {MESSAGE: "You don't have any news, go follow some authors, put some books into your collection"}, OK_STATUS
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class MyRatings(Resource):
    @login_required()
    def get(self):

        result, status = get_own_ratings()

        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "You have no rating, go read some books!"}, NOT_FOUND
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def post(self):
        rating_json = request.get_json()
        status = post_my_rating(rating_json)

        if status == OK_STATUS:
            return {MESSAGE: "Thank you for your opinion."}, OK_STATUS
        elif status == CONFLICT:
            return {MESSAGE: "You already left a rating for this book"}, CONFLICT
        elif status == BAD_REQUEST:
            return {MESSAGE: "Please provide valid stars and content for your rating."}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def put(self):
        rating_json = request.get_json()
        status = edit_my_rating(rating_json)

        if status == OK_STATUS:
            return {MESSAGE: "Your rating is updated"}, OK_STATUS
        elif status == NO_CONTENT:
            return {MESSAGE: "Your rating doesn't have any changes"}
        elif status == BAD_REQUEST:
            return {MESSAGE: "Please provide valid stars and content for your rating."}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class Subscribe(Resource):
    @login_required()
    def post(self):

        author_id = request.args.get(AUTHOR_ID)
        status = subscribe_to_author(author_id)
        if status == OK_STATUS:
            return {MESSAGE: "Thank you for your subscription!"}, OK_STATUS
        elif status == BAD_REQUEST:
            return {MESSAGE: "You can't subscribe to this author (probably because this author is just your illusion...)"}, BAD_REQUEST
        elif status == CONFLICT:
            return {MESSAGE: "You're already subscribed to this author"}, CONFLICT
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


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


class MyBookmarks(Resource):
    @login_required()
    def get(self):
        pass

    @login_required()
    def post(self, bm_name):
        pass

    @login_required()
    def put(self, bm_name):
        pass

    @login_required()
    def delete(self, bm_name):
        pass
