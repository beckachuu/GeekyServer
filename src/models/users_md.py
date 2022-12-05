from init_app import db
from src.const import *
from src.models.collections_md import Collections
from src.utils import (is_url_image, is_valid_datetime, is_valid_name,
                       is_valid_username, validate_phone)
from src.utils import get_username_from_email


class Users(db.Model):
    username = db.Column(db.String(64), primary_key=True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    profile_pic = db.Column(db.String)
    theme_preference = db.Column(db.Integer)
    login_state = db.Column(db.String)
    user_role = db.Column(db.Integer)
    restrict_due = db.Column(db.DateTime)
    recieve_email = db.Column(db.Integer)

    def __init__(self, email, profile_pic):
        self.username = get_username_from_email(email)
        self.email = email
        self.profile_pic = profile_pic
        self.theme_preference = 1
        self.user_role = 0
        self.recieve_email = 1

    def get_json(self):
        collections_query = Collections.query.filter_by(username=self.username)
        collection_list = []
        for collection in collections_query:
            collection_list.append(collection.get_json(
                self.username, collection.coll_name))

        return {
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'phone': self.phone,
            'profile_pic': self.profile_pic,
            'theme_preference': self.theme_preference,
            'collections': {"collection_list": collection_list,
                            "collection_count": len(collection_list)},
        }

    def update_username(self, new_username):
        if self.username != new_username and is_valid_username(new_username, 64):
            self.username = new_username
            return True
        return False

    def update_name(self, new_name):
        if self.name != new_name and is_valid_name(new_name):
            self.name = new_name
            return True
        return False

    def update_phone(self, new_phone):
        new_phone = validate_phone(new_phone)
        if self.phone != new_phone:
            self.phone = new_phone
            return True
        return False

    def update_profile_pic(self, new_pic_url):
        if self.profile_pic != new_pic_url and is_url_image(new_pic_url):
            self.profile_pic = new_pic_url
            return True
        return False

    def update_theme_preference(self, new_theme_pref):
        if self.theme_preference != new_theme_pref and isinstance(new_theme_pref, int):
            self.theme_preference = new_theme_pref
            return True
        return False

    def update_restrict_due(self, restrict_due):
        if self.restrict_due != restrict_due and is_valid_datetime(restrict_due):
            self.restrict_due = restrict_due
            return True
        return False

    def update_receive_email(self, receive_email):
        if self.recieve_email != receive_email and (receive_email == 0 or receive_email == 1):
            self.recieve_email = receive_email
            return True
        return False
