from flask import Flask
from manage import app
import config 
import sqlite3
from sqlalchemy import *

db = create_engine('sqlite:///bot.db')

# create app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.ProductionConfig)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app