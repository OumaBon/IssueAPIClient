from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS





db = SQLAlchemy()
cors = CORS()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Development")
    db.init_app(app)
    cors.init_app(app)
    
    from app.routes import api
    app.register_blueprint(api)
    return app 


