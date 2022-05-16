from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Codefly"), 200


@app.route('/articles/')
def articles():
    return render_template('articles.html', title="Codefly"), 200


@app.route('/about/')
def about():
    return render_template('about.html', title="Codefly"), 200


@app.route('/contact/')
def contact():
    return render_template('contact.html', title="Codefly"), 200


@app.route('/projects/')
def projects():
    return render_template('projects.html', title="Codefly"), 200


@app.route('/projects/chat/')
def chat():
    import bot as bot
    bot.x()
    return render_template('chat.html', title="Codefly"), 200


@app.route('/projects/gw2/', methods=['GET', 'POST'])
def gw2():
    return render_template('gw2.html', title="Codefly"), 200


# @app.errorhandler(Exception)
# def http_exception(e):
#     return render_template('404.html', e=e, title="404"), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e, title="404"), 404


if __name__ == "__main__":
    app.run(debug=True)

