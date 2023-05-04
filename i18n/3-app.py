#!/usr/bin/env python3
"""
aaaa
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _ as translation


class Config(object):
    """
    aaaa
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)



def get_locale():
    """

    :return:
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def root():
    """

    :return:
    """
    return render_template('/3-index.html',
                           title=translation('home_title'),
                           header=translation('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
