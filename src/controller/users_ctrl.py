import time

import google.auth.transport.requests
import requests
from flask import redirect, request
from flask_cors import cross_origin
from flask_restful import Resource
from google.oauth2 import id_token
from pip._vendor import cachecontrol

from init_app import db
from config.config import GOOGLE_CLIENT_ID, flow
from src.const import *
from src.controller.auth import get_current_user, admin_only, login_required, remove_current_state
from src.models.states_md import States
from src.models.users_md import Users
from src.services.users_sv import *
from src.utils import *


class Login(Resource):
    def get(self):
        authorization_url, state = flow.authorization_url()
        response = redirect(authorization_url)

        response.set_cookie(STATE, state)
        db.session.add(States(state))
        db.session.commit()
        # print("STATE FROM LOGIN(): ", state)  # gud

        return response


class Callback(Resource):
    # @cross_origin(supports_credentials=True)
    def get(self):
        # print("STATE AT BEGINNING OF CALLBACK(): ", request.cookies.get(STATE)) # wrong

        flow.fetch_token(authorization_response=request.url)
        response = redirect("/my_account")

        db_state = States.query.filter_by(
            state=request.args[STATE]).first().state
        if not db_state == request.args[STATE]:
            if db_state:
                remove_current_state()
            return {"message": "States don't match. You may delete your cookies and retry."}, 500

        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(
            session=cached_session)

        time.sleep(1.1)  # Avoid error "ValueError: Token used too early"
        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID
        )

        current_email = id_info.get(EMAIL)

        user = Users.query.filter_by(email=current_email).first()
        if user is None:
            user = Users(email=current_email)
            user.profile_pic = id_info.get(PICTURE)
            db.session.add(user)

        user.login_state = db_state
        db.session.commit()

        response.set_cookie(STATE, db_state)
        return response


class Logout(Resource):
    def get(self):
        remove_current_state()
        response = redirect("/")
        response.delete_cookie(STATE)
        return response


class MyAccount(Resource):
    @login_required()
    def get(self):
        userId = request.args.get('userId')

        account = get_own_account()
        if account is not None:
            return account.get_json(), OK_STATUS
        else:
            return {MESSAGE: "Account not found"}, NOT_FOUND

    @login_required()
    def post(self):
        request_args = request.args

        username = request_args.get(USERNAME)
        name = request_args.get(NAME)
        phone = request_args.get(PHONE)
        profile_pic = request_args.get(PROFILE_PIC)
        theme_preference = request_args.get(THEME)

        status = edit_own_account(username, name, phone,
                                  profile_pic, theme_preference)

        if status == OK_STATUS:
            return {MESSAGE: "Your profile is updated"}, OK_STATUS
        elif status == NO_CONTENT:
            return {MESSAGE: "Your profile is the same"}, OK_STATUS
        else:
            return {MESSAGE: "Account not found"}, NOT_FOUND


class ChangeRole(Resource):
    @admin_only()
    def get(self):
        username = request.args.get(USERNAME)
        role = request.args.get(USER_ROLE)

        user = Users.query.filter_by(username=username).first()
        if role == ADMIN:
            user.user_role = ADMIN
            db.session.commit()
            return {MESSAGE: "The admin team has a new member!"}
        if role == MUGGLE_USER:
            user.user_role = MUGGLE_USER
            db.session.commit()
            return {MESSAGE: "Another muggle!"}
        return {MESSAGE: "Please recheck the role you want this user to have"}
