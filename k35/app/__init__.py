'''
Java - DAL and DJM
SoftDev
K35: Now Again for the First Time
time spent: 4 hrs
'''

from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

def init_db():
    with sqlite3.connect('weblog.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Blog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                date_posted TEXT NOT NULL,
                content TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User (id)
            )
        ''')
        conn.commit()

@app.route('/')
def home():
    with sqlite3.connect('weblog.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Blog ORDER BY date_posted DESC')
        blogs = cursor.fetchall()
    
        user = None
        if 'user_id' in session:
            cursor.execute('SELECT * FROM User WHERE id = ?', (session['user_id'],))
            user = cursor.fetchone()
    return render_template('home.html', user=user, blogs=blogs)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        with sqlite3.connect('weblog.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash('Username already taken. Please choose a different username.', 'danger')
                return render_template('register.html')

            cursor.execute('INSERT INTO User (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            user_id = cursor.lastrowid

        session['user_id'] = user_id
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('weblog.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM User WHERE username = ?', (username,))
            user = cursor.fetchone()
            if user and check_password_hash(user[2], password):
                session['user_id'] = user[0]
                return redirect(url_for('home'))
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/create_blog', methods=['GET', 'POST'])
def create_blog():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date_posted = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect('weblog.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Blog (title, date_posted, content, user_id) VALUES (?, ?, ?, ?)', (title, date_posted, content, session['user_id']))
            conn.commit()
        return redirect(url_for('home'))
    return render_template('create_blog.html')

@app.route('/edit_blog/<int:blog_id>', methods=['GET', 'POST'])
def edit_blog(blog_id):
    with sqlite3.connect('weblog.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Blog WHERE id = ?', (blog_id,))
        blog = cursor.fetchone()
        if not blog or blog[4] != session.get('user_id'):
            return redirect(url_for('home'))
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            cursor.execute('UPDATE Blog SET title = ?, content = ? WHERE id = ?', (title, content, blog_id))
            conn.commit()
            return redirect(url_for('view_blog', blog_id=blog_id))
    return render_template('edit_blog.html', blog=blog)

@app.route('/view_blog/<int:blog_id>')
def view_blog(blog_id):
    with sqlite3.connect('weblog.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Blog WHERE id = ?', (blog_id,))
        blog = cursor.fetchone()
    return render_template('view_blog.html', blog=blog)

@app.route('/user_blogs/<int:user_id>')
def user_blogs(user_id):
    with sqlite3.connect('weblog.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM User WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        cursor.execute('SELECT * FROM Blog WHERE user_id = ? ORDER BY date_posted DESC', (user_id,))
        blogs = cursor.fetchall()
    return render_template('user_blogs.html', user=user, blogs=blogs)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)