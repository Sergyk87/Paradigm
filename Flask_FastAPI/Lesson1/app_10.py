from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "Hi!"


@app.route("/users/")
def users():
    _users = [
        {
            "name": "Никанор",
            "mail": "nik@mail.ru",
            "phone": "+7-999-565-66-32",
        },
        {
            "name": "Феофан",
            "mail": "feo@mail.ru",
            "phone": "+7-989-565-66-32",
        },
        {
            "name": "Оверранр",
            "mail": "forest@mail.ru",
            "phone": "+7-990-565-66-30",
        },
    ]

    context = {"user": _users, "title": "Точечная нотация"}
    return render_template("users.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
