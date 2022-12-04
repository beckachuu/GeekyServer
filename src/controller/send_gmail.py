import google.auth.transport.requests
import requests
from flask import redirect, request
from flask_cors import cross_origin
from flask_restful import Resource
from google.oauth2 import id_token
from pip._vendor import cachecontrol
from flask_mail import Mail, Message
from flask import Flask, make_response, jsonify

from config.config import GOOGLE_CLIENT_ID, flow
from init_app import db
from src.const import *
from src.controller.auth import remove_current_state
from src.models.states_md import States
from src.models.users_md import Users
from src.services.ratings_sv import *
from src.services.users_sv import *
from src.utils import *


class SendGmail(Resource):
    def get(self):
        # print("STATE AT BEGINNING OF CALLBACK(): ", request.cookies.get(STATE)) # wrong

        flow.fetch_token(authorization_response=request.url)

        db_state = States.query.filter_by(
            state=request.args[STATE]).first().state
        if not db_state == request.args[STATE]:
            if db_state:
                remove_current_state()
            return {"message": "States don't match. You may delete your cookies and retry."}, 500

        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(
            session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID,
            clock_skew_in_seconds=3
        )

        current_email = id_info.get(EMAIL)
        with app.app_context():
            msg = Message(subject="Hello",
                        sender='lam20020260@gmail.com',
                        # replace with your email for testing
                        recipients=["lam20020260@gmail.com"],
                        body="This is a test email I sent with Gmail and Python!")
            mail.send(msg)
            return make_response(jsonify({
                "message": "Email sent successfully"
            }))