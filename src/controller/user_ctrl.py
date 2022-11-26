from flask import request
from flask_restful import Resource

from init_app import db
from src.const import *
from src.controller.auth import get_current_user, admin_only, login_required
from src.models.users_md import Users
from src.services.users_sv import *
from src.utils import *
from src.services.ratings_sv import *


class MyAccount(Resource):
    @login_required()
    def get(self):
        account = get_own_account()
        if account is not None:
            return account.get_json(), OK_STATUS
        else:
            return {MESSAGE: "Account not found"}, NOT_FOUND

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
        elif status == NOT_FOUND:
            return {MESSAGE: "Account not found"}, NOT_FOUND
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class ChangeRole(Resource):
    @admin_only()
    def post(self):
        username = request.args.get(USERNAME)
        new_role = request.args.get(USER_ROLE)

        status = change_user_role(username, new_role)
        if status == NOT_FOUND:
            return {MESSAGE: "Can't find that user"}, NOT_FOUND
        elif status == CONFLICT:
            return {MESSAGE: "User already has this role"}, CONFLICT
        elif status == OK_STATUS:
            return {MESSAGE: "User's social status has changed!"}
        elif status == BAD_REQUEST:
            return {MESSAGE: "That's an invalid role..."}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class MyRatings(Resource):
    @login_required()
    def get(self):
        user = get_current_user()

        result, status = get_user_ratings(user.username)
        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "You have no rating, go read some books!"}, NOT_FOUND
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def post(self, rating_json):
        user = get_current_user()

        result, status = post_user_rating(user.username, rating_json)
        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "Can't post your rating"}, NOT_FOUND
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class Subscribe(Resource):
    @login_required()
    def post(self):
        user = get_current_user()
        username = user.username
        author_id = request.args.get(AUTHOR_ID)
        status = subscribe_to_author(username, author_id)
        if status == OK_STATUS:
            return {MESSAGE: "Thank you for your subscription!"}, OK_STATUS
        elif status == BAD_REQUEST:
            return {MESSAGE: "You can't subscribe to this author (probably because this author is just your illusion...)"}, BAD_REQUEST
        elif status == CONFLICT:
            return {MESSAGE: "You're already subscribed to this author"}, CONFLICT
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS


class BanUser(Resource):
    @admin_only()
    def post(self):
        restrict_info = request.get_json()
        username = restrict_info[USERNAME]
        restrict_due = restrict_info['restrict_due']

        status = ban_user(username, restrict_due)
        if status == OK_STATUS:
            return {MESSAGE: "This user is banned."}, OK_STATUS
        elif status == BAD_REQUEST:
            return {MESSAGE: "Please check the date you want this user to be unbanned"}, BAD_REQUEST
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS
