import os
import time
from functools import wraps

import google.auth.transport.requests
import requests
from flask import redirect, request, session
from flask_restful import Resource
from google.oauth2 import id_token
from pip._vendor import cachecontrol

from lib.config import GOOGLE_CLIENT_ID, flow
from src.const import EMAIL, NAME, STATE
from src.models.users_md import Users


def login_required():
    def wrapper(function):
        @wraps(function)
        def real_func(*args, **kwargs):
            cookies_state = request.cookies.get(STATE)
            # print("STATE IN LOGIN-REQUIRED(): ", request.cookies.get(STATE))  # gud

            if not request.cookies.get(EMAIL) or not cookies_state:
                return redirect("/login")
            else:
                user = Users.query.filter_by(login_state=cookies_state).first()
                if not user:
                    return redirect("/login")

            return function(*args, **kwargs)
        return real_func
    return wrapper


def admin_only():
    # TODO:
    def wrapper(function):
        @wraps(function)
        def real_func(*args, **kwargs):
            # if "google_id" not in session:
            #     return redirect("/login")
            # else:
            return function(*args, **kwargs)
        return real_func
    return wrapper


def reauthentication_required():
    # TODO:
    def wrapper(function):
        @wraps(function)
        def real_func(*args, **kwargs):
            # if "google_id" not in session:
            #     return redirect("/login")
            # else:
            return function(*args, **kwargs)
        return real_func
    return wrapper
