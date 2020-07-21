from flask import Flask, request, render_template
from stories import Story, story1, story2
from random import choice

app = Flask(__name__)

# stories = {story1.template:story1.prompts, story2.template:story2.prompts}
# prompts = stories.values()
stories = [story1, story2]


@app.route('/')
def home_page():
    """shows home page"""
    story = choice(stories)
    prompts = story.prompts
    text = story.template
    return render_template("home.html", story=story, prompts=prompts, text=text)

# @app.route('/story')
# def show_story():
#     """shows the finished story"""
    


