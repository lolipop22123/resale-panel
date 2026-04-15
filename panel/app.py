from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_here' # For session management

# Временная "база данных" для примера
USERS = {
    'admin': {'password': '123', 'is_admin': True},
    'user': {'password': '123', 'is_admin': False}
}

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('user_home'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        is_admin_request = 'is_admin' in request.form
        
        # Простая проверка (временно)
        if username in USERS and USERS[username]['password'] == password:
            session['user_id'] = username
            session['is_admin'] = USERS[username]['is_admin']
            
            if session['is_admin']:
                return redirect(url_for('admin_home'))
            else:
                return redirect(url_for('user_home'))
        
        flash('Неверный логин или пароль')
        return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Пользовательские маршруты
@app.route('/user/home')
def user_home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('user/home.html')

@app.route('/user/accounts')
def user_accounts():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('user/accounts.html')

# Административные маршруты
@app.route('/admin/home')
def admin_home():
    if 'user_id' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))
    return "<h1>Добро пожаловать в админ-панель! (В разработке)</h1><a href='/logout'>Выход</a>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
