import sqlalchemy as sql

from init_app import f_sql


class Users(f_sql.Model):
    username = sql.Column(sql.String, primary_key=True)
    email = sql.Column(sql.String)
    name = sql.Column(sql.String)
    phone = sql.Column(sql.String)
    profile_pic = sql.Column(sql.String)
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
        users = f_sql.session.execute(f_sql.select(Users).scalar())
