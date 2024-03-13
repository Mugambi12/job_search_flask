from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from app.backend.views.auth import auth_bp
from app.backend.views.jobs import jobs_bp

app.register_blueprint(auth_bp)
app.register_blueprint(jobs_bp)
