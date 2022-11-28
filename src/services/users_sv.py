import sqlalchemy
from flask import request
from sqlalchemy import delete

from init_app import db
from src.const import *
from src.const import EMAIL
from src.controller.auth import admin_only, login_required, remove_current_state, get_current_user
from src.models.bookmarks_md import Bookmark
from src.models.collections_md import Collections
from src.models.noti_md import Notifications
from src.models.ratings_md import Ratings
from src.models.subscription_md import Subscription
from src.models.users_md import Users
from src.utils import equal


def get_own_account(username):
    cookies_state = request.cookies.get(STATE)
    user = Users.query.filter_by(login_state=cookies_state).first()
    if user is None:
        return None, NOT_FOUND
    return user.get_json(), OK_STATUS


def edit_own_account(username, name, phone, profile_pic, theme_preference):
    user = get_current_user()
    updated = False

    if user is None:
        return None, NOT_FOUND

    if user.update_username(username):
        updated = True

    if user.update_name(name):
        updated = True

    if user.update_phone(phone):
        updated = True

    if user.update_profile_pic(profile_pic):
        updated = True

    if user.update_theme_preference(theme_preference):
        updated = True

    if updated:
        db.session.commit()
        return OK_STATUS

    return NO_CONTENT


def remove_own_account():
    user = get_current_user()
    try:
        username = user.username

        all_noti = Notifications.query.filter_by(username=username).all()
        all_subs = Subscription.query.filter_by(username=username).all()
        all_bookmark = Bookmark.query.filter_by(username=username).all()
        all_rating = Ratings.query.filter_by(username=username).all()

        to_delete = all_noti+all_bookmark+all_rating+all_subs
        for obj in to_delete:
            db.session.delete(obj)

        db.session.delete(user)
        remove_current_state()

        db.session.commit()
        return OK_STATUS
    except:
        return SERVER_ERROR


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


@admin_only()
def remove_rating():
    pass
