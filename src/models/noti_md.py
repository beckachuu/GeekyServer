from init_app import db


class Notifications(db.Model):
    noti_id = db.Column(db.Integer, primary_key=True)
    noti_text = db.Column(db.String)
    noti_date = db.Column(db.DateTime)
    trigger_source = db.Column(db.String)
    username = db.Column(db.String, db.ForeignKey('users.username'))

    def __init__(self, noti_text, noti_date, trigger_source, username):
        self.noti_text = noti_text
        self.noti_date = noti_date
        self.trigger_source = trigger_source
        self.username = username
