from init_app import db


class Bookmark(db.Model):
    username = db.Column(db.String, primary_key=True)
    book_id = db.Column(db.String(70))
    bm_name = db.Column(db.String)
    line_position = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, author_name,  profile_pic=None, bio=None, website=None, social_account=None):
        self.book_id = author_name
        self.bm_name = profile_pic
        self.line_position = bio
        self.content = social_account

    def get_json(self):
        return {
            'author_id': self.username,
            'author_name': self.book_id,
            'profile_pic': self.bm_name,
            'bio': self.line_position,
            'social_account': self.content,
        }
