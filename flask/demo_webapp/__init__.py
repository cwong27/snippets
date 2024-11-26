import os

from flask import Flask
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # SQLite URI
        SQLALCHEMY_DATABASE_URI='sqlite:///flaskr.sqlite', 
        # Disable event notifications
        SQLALCHEMY_TRACK_MODIFICATIONS=False,          
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # @app.route("/")
    # def default():
    #     return redirect(url_for("auth.login"))

    db.init_app(app)

    with app.app_context():
        # Ensure database tables are created
        from demo_webapp.models.User import User
        from demo_webapp.models.Blog import Blog
        db.create_all()

    # apply the blueprints to the app
    from demo_webapp.api import admin
    from demo_webapp.api import auth
    from demo_webapp.api import blog
    from demo_webapp.vulns import vulns

    app.register_blueprint(admin.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(vulns.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app