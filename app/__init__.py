from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create app
app = Flask(__name__)

# add database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
