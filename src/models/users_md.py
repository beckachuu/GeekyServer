from init_app import db
from src.models.collections_md import Collections
from src.utils import (get_username_from_email, is_url_image, is_valid_name,
                       is_valid_username, validate_phone)
from src.const import *


class Users(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    profile_pic = db.Column(db.String)
    theme_preference = db.Column(db.Integer)
    login_state = db.Column(db.String)
    user_role = db.Column(db.Integer)

    def __init__(self, email, name=None, phone=None, profile_pic=None, theme_preference=1, user_role=0):
        self.username = get_username_from_email(email)
        self.email = email
        self.name = name
        self.phone = phone
        self.profile_pic = profile_pic
        self.theme_preference = theme_preference
        self.user_role = user_role

    def get_json(self):
        collections_query = Collections.query.filter_by(username=self.username)
        collection_list = []
        for collection in collections_query:
            collection_list.append(collection.to_json())

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
        if self.username != new_username and is_valid_username(new_username):
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
        if self.theme_preference != new_theme_pref and new_theme_pref.isnumeric():
            self.theme_preference = new_theme_pref
            return True
        return False
