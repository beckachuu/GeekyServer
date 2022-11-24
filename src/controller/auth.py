from functools import wraps

from flask import redirect, request
from src.models.states_md import States
from init_app import db
from src.const import *
from src.models.users_md import Users
from src.utils import equal


def login_required():
    def wrapper(function):
        @wraps(function)
        def real_func(*args, **kwargs):
            cookies_state = request.cookies.get(STATE)
            # print("STATE IN LOGIN-REQUIRED(): ", request.cookies.get(STATE))  # gud

            if not cookies_state:
                # print("YOU DONT HAVE ANY COOKIE STATE")
                return redirect("/login")
            else:
                user = Users.query.filter_by(login_state=cookies_state).first()
                if not user:
                    # print("NO USER WITH THIS COOKIE STATE: ", cookies_state)
                    return redirect("/login")

            return function(*args, **kwargs)
        return real_func
    return wrapper


def admin_only():
    def wrapper(function):
        @wraps(function)
        def real_func(*args, **kwargs):
            cookies_state = request.cookies.get(STATE)

            if not cookies_state:
                return redirect("/login")
            else:
                user = Users.query.filter_by(login_state=cookies_state).first()
                if not user:
                    return redirect("/login")
                if not equal(user.user_role, ADMIN):
                    return {MESSAGE: "You shall not pass! ('cause you're not authorized)"}, UNAUTHORIZED

            return function(*args, **kwargs)
        return real_func
    return wrapper


def remove_current_state():
    cookies_state = request.cookies.get(STATE)
    state_db = States.query.filter_by(state=cookies_state).first()
    db.session.delete(state_db)
    db.session.commit()


def get_current_user():
    cookies_state = request.cookies.get(STATE)

    user = Users.query.filter_by(login_state=cookies_state).first()
    return user
