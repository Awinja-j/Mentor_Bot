from flask import Flask
from flask_restful import Api
from config import config
from manage import db
from app2.bot.bot import MentorBot



def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(MentorBot, '/bot')
    app.config.from_object(config[config_name])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


