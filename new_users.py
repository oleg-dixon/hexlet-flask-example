from flask import Flask, render_template, request, redirect, url_for
import json
import uuid
import os

app = Flask(__name__)

# Файл для хранения пользователей
USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

@app.route("/")
def hello_world():
    return "Welcome New User!"

@app.route("/users/new")
def users_new():
    user = {
        "name": "",
        "email": "",
    }
    errors = {}
    return render_template("users/new.html", user=user, errors=errors)

@app.route("/users", methods=['POST'])
def create_user():
    # Получаем данные из формы
    name = request.form.get('name')
    email = request.form.get('email')
    
    # Создаем пользователя с уникальным id
    user = {
        'id': str(uuid.uuid4()),  # Генерируем уникальный ID
        'name': name,
        'email': email
    }
    
    # Загружаем существующих пользователей
    users = load_users()
    # Добавляем нового пользователя
    users.append(user)
    # Сохраняем обратно в файл
    save_users(users)
    
    # Редирект на /users
    return redirect(url_for('list_users'))

@app.route("/users")
def list_users():
    users = load_users()
    return render_template("users/list.html", users=users)
