#!/usr/bin/env python3
"""
aaaa
"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config():
    """
    aaaa
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask()
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """

    :return:
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """

    :return:
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
