"""
Application Factory function will be created here, so that an instance of FLASK will be created inside the factory
function and returned rather than creating global FLASK instance, which causes tricky problems as application
grows bigger in time.
"""

import os
from flask import Flask


# Application Factory Function
def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:

        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return 'Hello World!'

    return app
