

class Development:
    DEBUG = True
    SECRET_KEY = "secreat"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True