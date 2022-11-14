import sqlalchemy as sql
from flask import redirect, request, session

from init_app import db
from src.models.users_md import Users
from src.const import STATE
from src.controller.auth import login_required,  reauthentication_required, admin_only
from src.const import EMAIL


def register_user():
    pass


@login_required()
def get_own_account():
    user = Users.query.filter_by(email=request.cookies.get(EMAIL)).first()
    return user.username


# @login_required()
def edit_own_account():
    pass


# @login_required()
def remove_own_account():
    pass


# @login_required()
def subscribe_to_author():
    pass


# @login_required()
def create_collection():
    pass


# @login_required()
def get_collections():
    pass


# @login_required()
def get_collection_by_name():
    pass


# @login_required()
def edit_collection_name(name=None):
    pass


# @login_required()
def remove_book_from_collections(book_id):
    pass


# @login_required()
def get_my_rates():
    pass


# @login_required()
def get_all_notis():
    pass


# @login_required()
def remove_noti(noti_id):
    pass


# @admin_only()
def get_user_info(username):
    pass


# @reauthentication_required()
# @admin_only()
def remove_user(username):
    pass


# @admin_only()
def add_book():
    pass


# @admin_only()
def edit_book_info():
    pass


# @admin_only()
def remove_book():
    pass


# @admin_only()
def remove_rating():
    pass
