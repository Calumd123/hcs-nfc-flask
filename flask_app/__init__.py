from flask import Flask 
from flask_cors import CORS
from .routes.app import app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(app)
    CORS(app)
    return app 
