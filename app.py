from flask import Flask, request, render_template, session, make_response
from stories import Story, story1, story2, story3
from random import choice, randint


app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"



stories = [story1, story2, story3]

@app.route('/')
def home_page():
    """shows home page"""
    random_number = randint(0, 2)
    session["random_number"] = random_number
    story = stories[random_number]
    prompts = story.prompts

    return render_template("home.html", prompts=prompts,)



@app.route('/story')
def show_story():
    """Show story result."""
    story = stories[session["random_number"]]
    text = story.generate(request.args)
    temp = story.template

    return render_template("story.html", text=text, temp=temp)



