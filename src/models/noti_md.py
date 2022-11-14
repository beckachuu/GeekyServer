import sqlalchemy as sql

from init_app import db


class Notifications(sql.Model):
    noti_id = sql.Column(sql.Integer, primary_key=True)
    noti_text = sql.Column(sql.String)
    noti_date = sql.Column(sql.DateTime)
    trigger_source = sql.Column(sql.String)
    username = sql.Column(sql.String, sql.ForeignKey('users.username'))

    def __init__(self, noti_id, noti_text, noti_date, trigger_source, username):
        self.noti_id = noti_id
        self.noti_text = noti_text
        self.noti_date = noti_date
        self.trigger_source = trigger_source
        self.username = username
