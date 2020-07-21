from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    """shows home page"""
    return render_template("home.html")