import sqlalchemy
from flask import request

from init_app import db
from src.const import *
from src.const import EMAIL
from src.controller.auth import admin_only, login_required
from src.models.ratings_md import Ratings
from src.models.subscription_md import Subscription
from src.models.users_md import Users
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


def subscribe_to_author(username, author_id):
    new_subscription = Subscription()
    if new_subscription.update_username(username) and new_subscription.update_author_id(author_id):
        try:
            db.session.add(new_subscription)
            db.session.commit()
            return OK_STATUS
        except sqlalchemy.exc.IntegrityError:
            return CONFLICT
    return BAD_REQUEST


@login_required()
def get_my_noti():
    pass


@login_required()
def change_noti_pref(noti_pref):
    pass


@admin_only()
def get_user_list():
    pass


def change_user_role(username, new_role):
    user = Users.query.filter_by(username=username).first()

    if user is None:
        return NOT_FOUND

    if equal(user.user_role, new_role):
        return CONFLICT

    if new_role == ADMIN or new_role == MUGGLE_USER:
        user.user_role = new_role
        db.session.commit()
        return OK_STATUS
    return BAD_REQUEST


def ban_user(username, restrict_due):
    user = Users.query.filter_by(username=username).first()
    if user is None:
        return NOT_FOUND

    if user.update_restrict_due(restrict_due):
        db.session.commit()
        return OK_STATUS
    return BAD_REQUEST


def remove_user(username):
    pass


# @admin_only()
# def remove_rating():
#     pass
