import keys
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pymongo
# from pymongo import MongoClient


app = Flask(__name__)
app.config['SECRET_KEY'] = keys.app_config_secret_key


@app.route('/')
def index():
    return render_template('index.html', title="Codefly"), 200


@app.route('/articles/')
def articles():
    return render_template('articles.html', title="Codefly - Articles"), 200


@app.route('/about/')
def about():
    return render_template('about.html', title="Codefly - About"), 200


@app.route('/contact/')
def contact():
    return render_template('contact.html', title="Codefly - Contact"), 200


@app.route('/projects/')
def projects():
    return render_template('projects.html', title="Codefly - Projects"), 200


@app.route('/projects/chat/')
def chat():
    form = BotForm()
    return render_template('chat.html', title="Codefly - Chatbot!", form=form), 200


@app.route('/send/', methods=['GET', 'POST'])
async def send():
    import bot
    default_value = "hi"
    user = request.form.get('send', default_value)
    return bot.reply(user) or "I don't understand."
    # return "x" if bot.reply(user) is None else bot.reply(user)


class BotForm(FlaskForm):
    chat = StringField(validators=[DataRequired()], name="send")
    submit = SubmitField('Send')


@app.route('/projects/gw2/', methods=['GET', 'POST'])
def gw2():
    return render_template('gw2.html', title="Codefly - Guild Wars 2 Logs"), 200


# @app.errorhandler(Exception)
# def http_exception(e):
#     return render_template('404.html', e=e, title="404"), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e, title="404"), 404


if __name__ == "__main__":
    app.run(debug=True)

