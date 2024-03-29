from flask import Flask
from Lesson3.models_05 import db, User, Post, Comment

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db.init_app(app)


@app.route("/")
def index():
    return "Hi!"


@app.cli.command("init-db")
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all()
    print("OK")


@app.cli.command("add-john")
def add_user():
    user = User(username="john", email="john@example.com")
    db.session.add(user)
    db.session.commit()
    print("John add in DB!")


if __name__ == "__main__":
    app.run(debug=True)
