import sqlalchemy as sql
from flask import redirect, request, session

from init_app import f_sql
from lib.config import flow
from src.const import STATE
from src.controller.auth import login_required, not_logged_in_required, reauthentication_required, admin_only


class GuestService:
    def register_user():
        pass

    @not_logged_in_required()
    def login():
        print("Login session ID: ", session.sid)

        authorization_url, state = flow.authorization_url()
        response = redirect(authorization_url)
        print("old session state: ", session.get(STATE))

        session[STATE] = state
        session.modified = True
        response.set_cookie(STATE, state)

        print("new session state: ", session.get(STATE))
        return response


@login_required
class UsersService:
    def logout():
        session.clear()
        return redirect("/")

    def remove_own_account():
        pass

    def subscribe_to_author():
        pass

    def edit_info():
        pass

    def create_collection():
        pass

    def get_collections():
        pass

    def get_collection_by_name():
        pass

    def edit_collection_name(name=None):
        pass

    def remove_book_from_collections(book_id):
        pass

    def get_my_rates():
        pass

    def get_all_notis():
        pass

    def remove_noti(noti_id):
        pass


@admin_only
class AdminService:
    def get_user_info(username):
        pass

    @reauthentication_required
    def remove_user(username):
        pass

    def add_book():
        pass

    def edit_book_info():
        pass

    def remove_book():
        pass

    def remove_rating():
        pass
