from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_httpauth import HTTPDigestAuth
from config import FlaskConfig

app = Flask(__name__)
app.config.from_object(FlaskConfig)
bootstrap = Bootstrap5(app)

auth = HTTPDigestAuth()
@auth.get_password
def get_pw(uname):
	return app.config['AUTH_USERS'].get(uname,None)

from app import routes