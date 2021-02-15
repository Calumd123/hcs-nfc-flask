from flask import Flask 
from flask_cors import CORS
from .routes.app import app

def create_app():
    webapp = Flask(__name__)
    webapp.register_blueprint(app)
    CORS(webapp)
    return webapp 
