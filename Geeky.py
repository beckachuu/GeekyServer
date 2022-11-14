import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from init_app import *
from src.controller.books_ctrl import *
from src.controller.users_ctrl import Callback, Login, Logout, ManageAccount
from src.models.states_md import States

# this is to set our environment to https because OAuth 2.0 only supports https environments
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


# db = SQLAlchemy()
# db.init_app(app)

api = Api(app)
api.add_resource(MainPage, '/')
api.add_resource(Login, '/login')
api.add_resource(Callback, '/callback')
api.add_resource(Logout, '/logout')

api.add_resource(ManageAccount, '/my_account')


api.add_resource(Search, '/search_result')


if __name__ == '__main__':
    app.run(debug=True)
