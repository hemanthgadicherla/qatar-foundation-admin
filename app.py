from flask import Flask, render_template
from config import Config
from models import db, Admin
from routes import init_routes
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, supports_credentials=True)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return {"error": "Login required"}, 401


@app.route('/')
def home():
    return render_template('admin.html')


@app.route('/login', methods=['GET'])
def login_page():
    return render_template('admin.html')


init_routes(app)

import os

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)