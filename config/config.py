from datetime import timedelta
import os
from google_auth_oauthlib.flow import Flow

client_secrets_file = os.path.join("lib/client_secret.json")

flow = Flow.from_client_secrets_file(  # Flow is OAuth 2.0 a class that stores all the information on how we want to authorize our users
    client_secrets_file=client_secrets_file,

    # here we are specifing what do we get after the authorization
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

USE_CREDENTIALS = True

# SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/w22g7_geek'
# For phpmyadmin:
SQLALCHEMY_DATABASE_URI = 'mysql://w22g7@10.244.2.172:3306/w22g7_geek'

SESSION_TYPE = 'filesystem'
SESSION_PERMANENT = True
# PERMANENT_SESSION_LIFETIME = timedelta(hours=5)

SECRET_KEY = 'justasimplesecretkeyhere'
GOOGLE_CLIENT_ID = "482973633382-tbr5icbjn9f895loe0a0iv7sgvsm0948.apps.googleusercontent.com"
CORS_HEADERS = 'Content-Type'
