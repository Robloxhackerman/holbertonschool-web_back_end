#!/usr/bin/env python3
"""
aaaa
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config():
    """
    aaaa
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    :return:
    """
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    :return:aaa
    """
    return render_template('2-index.html', title=_('title_header'), header=_('title_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
