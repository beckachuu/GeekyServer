import os
import pathlib
import time

import google.auth.transport.requests
import requests
from flask import Flask, abort, redirect, request, session
from flask_cors import CORS
from flask_restful import Api
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol

from src.controller.users import Testing


app = Flask(__name__)

#it is necessary to set a password when dealing with OAuth 2.0
app.secret_key = "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"  

 #this is to set our environment to https because OAuth 2.0 only supports https environments
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "482973633382-tbr5icbjn9f895loe0a0iv7sgvsm0948.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "env\client_secret.json")

flow = Flow.from_client_secrets_file(  #Flow is OAuth 2.0 a class that stores all the information on how we want to authorize our users
    client_secrets_file=client_secrets_file,

    #here we are specifing what do we get after the authorization
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"  #and the redirect URI is the point where the user will end up after the authorization
)



@app.route("/")  
def index():
    return "Hello World <a href='/login'><button>Login</button></a>"

@app.route("/login") 
def login():
    authorization_url, state = flow.authorization_url() 
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session.get("state") == request.args["state"]:
        abort(500)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)


    time.sleep(1) # Avoid ValueError: Token used too early
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    print("id_info: ", id_info)

    session["google_id"] = id_info.get("sub")  #defing the results to show on the page
    session["name"] = id_info.get("name")
    return redirect("/protected_area")  #the final page where the authorized users will end up


@app.route("/logout") 
def logout():
    session.clear()
    return redirect("/")


def login_is_required(function): 
    def wrapper(*args, **kwargs):
        if "google_id" not in session: 
            return abort(401)
        else:
            return function()
    return wrapper

@app.route("/protected_area")
@login_is_required
def protected_area():
    return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"  #the logout button 



#########################################################################

CORS(app)
app.config.from_pyfile('src/core/config.py')
api = Api(app)

api.add_resource(Testing, '/test')


if __name__ == '__main__':
    app.run(debug=True)



