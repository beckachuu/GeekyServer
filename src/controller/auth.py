from datetime import datetime
from functools import wraps

from flask import redirect, request

from config.config import FRONTEND_URL
from init_app import db
from src.const import *
from src.models.states_md import States
from src.models.users_md import Users
from src.utils import equal


def login_required():
    def wrapper(function):
        @wraps(function)
        def real_func(*args, **kwargs):
            cookies_state = request.get_json()[STATE]

            if not cookies_state:
                return redirect(f"{FRONTEND_URL}/login")
            else:
                user = Users.query.filter_by(login_state=cookies_state).first()
                if not user:
                    return redirect(f"{FRONTEND_URL}/login")
                if user.restrict_due is not None:
                    if user.restrict_due < datetime.today():
                        user.restrict_due = None
                        db.session.commit()
                    else:
                        return {MESSAGE: "Your account is restricted."}, FORBIDDEN

            return function(*args, **kwargs)
        return real_func
    return wrapper


def admin_only():
    def wrapper(function):
        @wraps(function)
        def real_func(*args, **kwargs):
            cookies_state = request.get_json()[STATE]

            if not cookies_state:
                return redirect(f"{FRONTEND_URL}/login")
            else:
                user = Users.query.filter_by(login_state=cookies_state).first()
                if not user:
                    return redirect(f"{FRONTEND_URL}/login")
                if not equal(user.user_role, ADMIN):
                    return {MESSAGE: "You shall not pass! ('cause you're not authorized)"}, FORBIDDEN

            return function(*args, **kwargs)
        return real_func
    return wrapper


# def remove_current_state():
#     cookies_state = request.cookies.get(STATE)
#     state_db = States.query.filter_by(state=cookies_state).first()
#     if state_db:
#         db.session.delete(state_db)
#         db.session.commit()


def get_current_user():
    cookies_state = request.cookies.get(STATE)
    user = Users.query.filter_by(login_state=cookies_state).first()
    if user is None:
        return redirect(f"{FRONTEND_URL}/login")
    return user
