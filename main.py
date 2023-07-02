from flask import Flask, render_template, request, redirect, url_for, make_response
from pathlib import PurePath, Path

from werkzeug.sansio import response

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/square', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        num = int(request.form.get('num'))
        return f"Квадрат числа {num} = {num * num}"
    return render_template('square.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        response = redirect(url_for("hello", name=username))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        return response
    return render_template('login.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/log_out')
def log_out():
    response = redirect(url_for('login'))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == "__main__":
    app.run(debug=True)