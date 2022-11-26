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
            return {MESSAGE: "We've encountered a problem"}, BAD_REQUEST


class ChangeRole(Resource):
    @admin_only()
    def post(self):
        username = request.args.get(USERNAME)
        new_role = request.args.get(USER_ROLE)

        user = Users.query.filter_by(username=username).first()
        if user is None:
            return {MESSAGE: "Can't find that user"}, NO_CONTENT

        if equal(user.user_role, new_role):
            return {MESSAGE: "User already has this role"}, BAD_REQUEST

        if new_role == ADMIN:
            user.user_role = ADMIN
            db.session.commit()
            return {MESSAGE: "The admin team has a new member!"}
        if new_role == MUGGLE_USER:
            user.user_role = MUGGLE_USER
            db.session.commit()
            return {MESSAGE: "Another muggle!"}
        return {MESSAGE: "Please recheck the role you want this user to have"}


class MyRatings(Resource):
    @login_required()
    def get(self):
        user = get_current_user()

        result, status = get_user_ratings(user.username)
        if status == OK_STATUS:
            return result, OK_STATUS
        else:
            return {MESSAGE: "You have no rating, go read some books!"}, NOT_FOUND

    @login_required()
    def post(self, rating_json):
        user = get_current_user()

        result, status = post_user_rating(user.username, rating_json)
        if status == OK_STATUS:
            return result, OK_STATUS
        else:
            return {MESSAGE: "Can't post your rating"}, NOT_FOUND


class Subscribe(Resource):
    @login_required()
    def post(self):
        user = get_current_user()
        username = user.username
        author_id = request.args.get(AUTHOR_ID)
        status = subscribe_to_author(username, author_id)
        if status == OK_STATUS:
            return {MESSAGE: "Thank you for your subscription!"}, OK_STATUS
        return {MESSAGE: "You can't subscribe to this author (probably because this author is just your illusion...)"}, BAD_REQUEST


class BanUser(Resource):
    @admin_only()
    def post(self, user_id, ban_length):
        pass
