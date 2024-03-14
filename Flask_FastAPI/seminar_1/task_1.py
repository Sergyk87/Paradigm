# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact"
#
@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.

@app.route('/<int:num_1>/<int:num_2>')
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.

@app.route('/string/<string:name>')
def text(name: str):
    return str(len(name))


# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

@app.route('/world')
def world():
    return render_template('index.html')


# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.


@app.route('/students/')
def students():
    head = {
        'firstname': 'Имя',
        'lastname': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл'
    }

    students_list = [
        {
            'firstname': 'Иван',
            'lastname': 'Иванов',
            'age': 18,
            'rating': 4
        },
        {
            'firstname': 'Петр',
            'lastname': 'Петров',
            'age': 19,
            'rating': 5
        },
        {
            'firstname': 'Сергей',
            'lastname': 'Сергеев',
            'age': 17,
            'rating': 6
        }]

    return render_template('index.html', **head, students_list=students_list)


# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

@app.route('/news/')
def news():
    news_block = [
        {
            'title': 'новость_1',
            'description': 'описание_1',
            'create_at': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
        },
        {
            'title': 'новость_2',
            'description': 'описание_2',
            'create_at': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
        },
        {
            'title': 'новость_3',
            'description': 'описание_3',
            'create_at': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
        }]

    return render_template('news.html', news_block=news_block)

# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.



if __name__ == '__main__':
    app.run(debug=True)
