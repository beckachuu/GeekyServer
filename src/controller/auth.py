import os
import time
from functools import wraps

import google.auth.transport.requests
import requests
from flask import redirect, request, session
from flask_cors import cross_origin
from flask_restful import Resource
from google.oauth2 import id_token
from pip._vendor import cachecontrol

from lib.config import GOOGLE_CLIENT_ID, flow
from src.const import NAME


def login_required():
    def wrapper(function):
        @wraps(function)
        def real_func(*args, **kwargs):
            if "google_id" not in session:
                return redirect("/login")
            else:
                return function(*args, **kwargs)
        return real_func
    return wrapper


def not_logged_in_required():
    # TODO:
    pass


@login_required
def admin_only():
    # TODO:
    pass


def reauthentication_required():
    # TODO:
    pass


class Callback(Resource):
    @cross_origin(supports_credentials=True)
    def get(self):
        print("Callback session ID: ", session.sid)

        flow.fetch_token(authorization_response=request.url)
        response = redirect("/search_result")

        # BUG HERE, uncomment this when you know how to fix
        # if not (request.cookies.get(STATE) == request.args[STATE]):
        #     saved_state = request.cookies.get(STATE)
        #     request_state = request.args[STATE]
        #     return {"message": "States don't match", "session_state": saved_state, "request_state": request_state}, 500

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

        session["google_id"] = id_info.get("sub")
        session[NAME] = id_info.get(NAME)
        return response
