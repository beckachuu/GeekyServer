from init_app import db
from src.utils import *


class Bookmark(db.Model):
    username = db.Column(db.String, primary_key=True)
    book_id = db.Column(db.String(70))
    bm_name = db.Column(db.String)
    line_position = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, username,  book_id, bm_name, line_position=None, content=None):
        self.username = username
        self.book_id = book_id
        self.bm_name = bm_name
        self.line_position = line_position
        self.content = content

    def get_json(self):
        return {
            'username': self.username,
            'book_id': self.book_id,
            'bm_name': self.bm_name,
            'line_position': self.line_position,
            'content': self.content,
        }

    def update_bm_name(self, new_bm_name):
        if self.bm_name != new_bm_name and is_valid_name(new_bm_name):
            self.bm_name = new_bm_name
            return True
        return False

    def update_line_pos(self, new_line_pos):
        if self.line_position != new_line_pos and new_line_pos.isnumeric():
            self.line_position = new_line_pos
            return True
        return False

    def update_content(self, new_content):
        if self.content != new_content and is_valid_text(new_content):
            self.content = new_content
            return True
        return False
