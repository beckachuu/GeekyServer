from datetime import timedelta
import os
from google_auth_oauthlib.flow import Flow

client_secrets_file = os.path.join("config/client_secret.json")

flow = Flow.from_client_secrets_file(  # Flow is OAuth 2.0 a class that stores all the information on how we want to authorize our users
    client_secrets_file=client_secrets_file,

    # here we are specifing what do we get after the authorization
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:5000/callback"
    # redirect_uri="http://w22g7.int3306.freeddns.org/callback"
)

USE_CREDENTIALS = True

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/w22g7_geek'

# For phpmyadmin:
# SQLALCHEMY_DATABASE_URI = 'mysql://w22g7:qwertyuiop@10.102.18.99:3306/w22g7_geek'


FRONTEND_URL = "http://localhost:3000"

SECRET_KEY = 'justasimplesecretkeyhere'
GOOGLE_CLIENT_ID = "482973633382-tbr5icbjn9f895loe0a0iv7sgvsm0948.apps.googleusercontent.com"
CORS_HEADERS = 'Content-Type'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'lam20020260@gmail.com'
MAIL_PASSWORD = 'lam2452002'

RECOMMEND_PATH = 'src/data/recommend.json'
