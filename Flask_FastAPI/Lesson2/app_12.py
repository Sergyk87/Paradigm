from pathlib import PurePath, Path

from flask import Flask, request, render_template, flash, url_for
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__)
app.secret_key = b'396641b4cbcaaf57a7f6fbaced750e851f4a3fff8d81365d0423989e2de4db82'
"""
Генерация надежного секретного ключа в Python Console
>>> import secrets
>>> secrets.token_hex
"""

@app.route('/')
def index():
    return 'Hi!'

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')

if __name__ == '__main__':
    app.run(debug=True)