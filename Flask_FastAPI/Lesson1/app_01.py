from flask import Flask


app = Flask(__name__)
#__name__ - передача названия файла



@app.route('/')
# приложение app использует метод route в качестве декоратора
# этот метод принимает в качестве аргумента параметр строки('/')
def hello_world():
    return 'Hello World (>^.^<)'
    #return 42
# flask не может вернуть число


if __name__ == '__main__':
    app.run()