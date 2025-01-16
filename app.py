from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route("/")
def intro():
    return "<h2>Introduction<h2>"

@app.route("/home")
def home():
    return "<h2>Home<h2>"

@app.route("/user/<user>") # path params <user> is string
def user(user):
    return f"<p>Hi, {escape(user)}!</P>"

@app.route("/user/<int:user_id>") # path params <user_id> is int
def userID(user_id):
    return f"<p>Hi, {user_id}!</P>"

@app.route("/price/<float:Price>") # path params <Price> is float
def invoice(Price):
    return f"<p>Current Price is, {Price}!</P>"

@app.route("/url/<path:urlPath>") # path params <urlPath> is path, which accepts / also
def urlpatter(urlPath):
    return f"<p>next Link is, {urlPath}!</P>"

@app.route("/random/<uuid:id>") # path params <id> is UUID
def value(id):
    return f"<p>New UUID is, {id}!</P>"

@app.route('/html')
def html():
    conn = get_db_connection()
    users = conn.execute('select * from user').fetchall()
    conn.close()
    return render_template("test.html", users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        conn.execute(f'insert into user (name) values (?)',
                     (name,))
        conn.commit()
        conn.close()
        return redirect(url_for('html'))
    return render_template('create.html')