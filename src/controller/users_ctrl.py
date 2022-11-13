import google.auth.transport.requests
import requests
from flask import redirect, request, session
from flask_restful import Resource

from init_app import f_sql
from src.const import MESSAGE
from src.controller.auth import login_required
from src.models.users_md import Users
from src.utils import *


class User(Resource):
    def get(self, username):
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return {MESSAGE: "No user found"}, 400
        return {MESSAGE: user.username}, 200

    def post(self):
        user = Users(
            username=random_string(),
            email=random_string(),
        )
        f_sql.session.add(user)
        f_sql.session.commit()
        return {MESSAGE: user.username}, 200
