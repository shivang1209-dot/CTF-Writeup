from flask import Flask, render_template, request, make_response, redirect, url_for
import base64
import json
import os

flag = os.getenv("FLAG", "bctf{fake_flag}")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "")
        cookie_data = {"name": name, "is_pharaoh": False}
        encoded = base64.b64encode(json.dumps(cookie_data).encode()).decode()

        response = make_response(redirect(url_for("tomb")))
        response.set_cookie("session", encoded)
        return response

    return render_template("index.html")


@app.route("/tomb")
def tomb():
    session_cookie = request.cookies.get("session")
    if not session_cookie:
        return redirect(url_for("home"))
    try:
        user = json.loads(base64.b64decode(session_cookie).decode())
    except Exception:
        return redirect(url_for("home"))
    return render_template("tomb.html", user=user, flag=flag)


@app.route("/logout")
def logout():
    response = make_response(redirect(url_for("home")))
    response.set_cookie("session", "", expires=0)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
