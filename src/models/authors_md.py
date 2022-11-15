from init_app import db


class Authors(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(70))
    profile_pic = db.Column(db.String)
    bio = db.Column(db.String)
    social_account = db.Column(db.String)
    website = db.Column(db.String)

    def __init__(self, author_name,  profile_pic=None, bio=None, website=None, social_account=None):
        self.author_name = author_name
        self.profile_pic = profile_pic
        self.bio = bio
        self.social_account = social_account
        self.website = website

    def get_json(self):
        return {
            'author_id': self.author_id,
            'author_name': self.author_name,
            'profile_pic': self.profile_pic,
            'bio': self.bio,
            'social_account': self.social_account,
            'website': self.website,
        }
