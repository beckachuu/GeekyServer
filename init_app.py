from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session

app = Flask(__name__)

app.config.from_pyfile('lib/config.py')
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
Session(app)
CORS(app)

f_sql = SQLAlchemy()
f_sql.init_app(app)
