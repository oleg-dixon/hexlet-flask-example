from flask import Flask, render_template, request
import logging
# Это callable WSGI-приложение
app = Flask(__name__)


users = [
    {"id": 1, "name": "mike"},
    {"id": 2, "name": "mishel"},
    {"id": 3, "name": "adel"},
    {"id": 4, "name": "keks"},
    {"id": 5, "name": "kamila"},
]


app.logger.setLevel(logging.DEBUG)


@app.route('/')
def index():
    app.logger.info(f'Получен запрос к главной странице')
    return 'Добро пожаловать!'

@app.route('/error')
def error():
    app.logger.info(f'Произошла ошибка')
    return 'Ошибка!', 500

@app.route("/")
def hello_world():
    return "Welcome to Flask!"


@app.route('/users/')
def get_users():
    term = request.args.get('term', '')
    print(users)
    filtered_users = [user for user in users if term in user['name']]
    return render_template(
        'users/index.html',
        users=filtered_users,
        search=term,
    )


@app.post("/users")
def users_post():
    return "POST /users"


@app.route("/courses/<id>")
def courses_show(id):
    return f"Course id: {id}"
