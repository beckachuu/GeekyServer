from init_app import db


class Subscription(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))

    def __init__(self, author_name,  username):
        self.author_name = author_name
        self.username = username

    # def get_json(self):
    #     return {
    #         'author_id': self.author_id,
    #         'username': self.username,
    #     }
