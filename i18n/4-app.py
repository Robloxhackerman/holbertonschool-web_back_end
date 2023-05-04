#!/usr/bin/env python3
"""
aaaa
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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

    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in Config.LANGUAGES:
            return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'], strict_slashes=False)
def root():
    """

    :return:
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)