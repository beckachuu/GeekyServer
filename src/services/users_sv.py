import sqlalchemy as sql
from flask import request

from init_app import db
from src.models.users_md import Users
from src.const import *
from src.controller.auth import login_required, admin_only
from src.const import EMAIL
from src.utils import equal


@login_required()
def get_own_account():
    cookies_state = request.cookies.get(STATE)
    user = Users.query.filter_by(login_state=cookies_state).first()
    return user


@login_required()
def edit_own_account(username=None, name=None, phone=None, profile_pic=None, theme_preference=None):
    account = get_own_account()
    updated = False

    # TODO: handle MySQLdb.DataError: (1406, "Data too long for column...)

    if account is None:
        return None, NOT_FOUND

    if account.update_username(username):
        updated = True

    if account.update_name(name):
        updated = True

    if account.update_phone(phone):
        updated = True

    if account.update_profile_pic(profile_pic):
        updated = True

    if account.update_theme_preference(theme_preference):
        updated = True

    if updated:
        db.session.commit()
        return OK_STATUS

    return NO_CONTENT


@login_required()
def remove_own_account():
    pass


@login_required()
def subscribe_to_author():
    pass


@login_required()
def create_collection():
    pass


@login_required()
def get_collections():
    pass


@login_required()
def get_collection_by_name():
    pass


@login_required()
def edit_collection_name(name=None):
    pass


@login_required()
def remove_book_from_collections(book_id):
    pass


@login_required()
def get_my_rates():
    pass


@login_required()
def get_my_noti():
    pass


@login_required()
def change_noti_pref(noti_pref):
    pass


@admin_only()
def get_user_list():
    pass


@admin_only()
def change_user_role(username, new_role):
    pass


@admin_only()
def remove_user(username):
    pass


@admin_only()
def add_book():
    pass


# @admin_only()
# def edit_book_info():
#     pass


@admin_only()
def remove_book():
    pass


# @admin_only()
# def remove_rating():
#     pass
