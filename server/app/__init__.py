from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config





db = SQLAlchemy()
cors = CORS()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    cors.init_app(app)
    
    from app.routes import api
    app.register_blueprint(api)
    return app 


