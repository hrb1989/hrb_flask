from flask import Flask
from markupsafe import escape

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