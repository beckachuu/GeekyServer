import sqlalchemy as sql

from init_app import db


class Users(db.Model):
    username = sql.Column(sql.String, primary_key=True)
    email = sql.Column(sql.String)
    name = sql.Column(sql.String)
    phone = sql.Column(sql.String)
    profile_pic = sql.Column(sql.String)
    theme_preference = sql.Column(sql.Integer)
    login_state = sql.Column(sql.String)
    user_role = sql.Column(sql.Integer)

    def __init__(self, username, email, name=None, phone=None, profile_pic=None, login_state=None, user_role=0):
        self.username = username
        self.email = email
        self.name = name
        self.phone = phone
        self.profile_pic = profile_pic
        self.user_role = user_role

    def get_user():
        users = db.session.execute(db.select(Users).scalar())
