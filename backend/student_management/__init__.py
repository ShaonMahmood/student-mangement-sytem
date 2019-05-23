from flask import Flask


def create_app(config_class=None):
    # create and configure the app
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)

    from student_management.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app
