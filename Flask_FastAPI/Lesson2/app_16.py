from flask import (
    Flask,
    request,
    make_response,
    render_template,
    session,
    redirect,
    url_for,
)

app = Flask(__name__)
app.secret_key = "396641b4cbcaaf57a7f6fbaced750e851f4a3fff8d81365d0423989e2de4db82"


@app.route("/")
def index():
    if "username" in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for("login"))


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username") or "NoName"
        return redirect(url_for("index"))
    return render_template("username_form.html")


@app.route("/logout/")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
