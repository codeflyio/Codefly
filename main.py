from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import keys

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
    import bot
    bot.x()
    return render_template('chat.html', title="Codefly - Chatbot!"), 200


@app.route('/speak/', methods=['GET', 'POST'])
def send():
    import bot as bot
    bot.x()
    default_value = "hi"
    user_input = request.form.get('user_input', default_value)
    return bot.reply(user_input)


class BotForm(FlaskForm):
    chat = StringField(validators=[DataRequired()])
    submit = SubmitField('Send!')


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

