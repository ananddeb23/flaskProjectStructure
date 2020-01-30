# Import flask and template operators
from flask import Flask, abort

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return abort(404)

# Import a module / component using its blueprint handler variable (module_one)
from app.module_one.controllers import mod_one as module_one

# Register blueprint(s)
app.register_blueprint(module_one)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()