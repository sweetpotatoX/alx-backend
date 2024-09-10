#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask import Flask, render_template
from flask_babel import Babel

babel = Babel()


class Config:
    """Config class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        """Retrieves the locale for a web page.
"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

    @app.route('/')
    def index():
        """Return the index page.
        """
        return render_template('2-index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
