import os
from student_management import create_app
from config import Config


"""
    Unfortunately, there is no direct support for application factory functions in the new Flask CLI. 
    The approach that you need to follow to use a factory function is to define a module that calls the 
    factory function to create the app object, and then reference that module in FLASK_APP. 
    This is similar in concept to the wsgi.py module in Django applications.

    Similarly for adding logger we can override the default logging handlers here 
"""
app = create_app(config_class=Config)


if __name__ == "__main__":
    app.run(debug=True)
