from turtle import color
from app import app

@app.route("/")
def hello():
    return "Hello, World."