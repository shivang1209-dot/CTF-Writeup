from flask import render_template, request as r, jsonify
from requests.auth import HTTPDigestAuth
from app import app, auth
import requests
 
@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/auth',methods=['GET'])
@auth.login_required
def auth():
    return render_template("auth.html",flag=app.config['FLAG'])

@app.route('/api/check',methods=['GET'])
def check():
    (user, pw), *_ = app.config['AUTH_USERS'].items()
    res = requests.get(r.referrer + '/auth',
        auth = HTTPDigestAuth(user,pw),
        timeout=3
    )
    return jsonify({'status':res.status_code})
