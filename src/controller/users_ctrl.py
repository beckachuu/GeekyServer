import time

import google.auth.transport.requests
import requests
from flask import redirect, request
from flask_cors import cross_origin
from flask_restful import Resource
from google.oauth2 import id_token
from pip._vendor import cachecontrol

from init_app import db
from lib.config import GOOGLE_CLIENT_ID, flow
from src.const import EMAIL, MESSAGE, NAME, STATE
from src.controller.auth import (admin_only, login_required,
                                 reauthentication_required)
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
    @cross_origin(supports_credentials=True)
    def get(self):
        # print("STATE AT BEGINNING OF CALLBACK(): ", request.cookies.get(STATE)) # wrong

        flow.fetch_token(authorization_response=request.url)
        response = redirect("/my_account")

        db_state = States.query.filter_by(
            state=request.args[STATE]).first().state
        if not db_state == request.args[STATE]:
            return {"message": "States don't match"}, 500

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

        user = Users.query.filter_by(email=id_info.get(EMAIL)).first()
        user.login_state = db_state

        print("adding user login state: ", user.login_state)

        db.session.commit()

        response.set_cookie(STATE, db_state)
        response.set_cookie(EMAIL, user.email)
        return response


class Logout(Resource):
    def get(self):
        cookies_state = request.cookies.get(STATE)
        print("Before log out state: ", cookies_state)

        state_db = States.query.filter_by(state=cookies_state).first()
        db.session.delete(state_db)

        db.session.commit()
        return redirect("/")


class ManageAccount(Resource):
    @login_required()
    def get(self):
        account = get_own_account()
        if account is not None:
            return get_own_account(), 200
        else:
            return {MESSAGE: "Account not found"}, 404
