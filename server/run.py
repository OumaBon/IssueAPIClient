import os
from dotenv import load_dotenv
from app import create_app, db

load_dotenv()
config_name = os.getenv('FLASK_CONFIG') or 'default'

app = create_app(config_name)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)


