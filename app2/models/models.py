from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Mentor(db.Model):
    __tablename__ = "mentor"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    stack = db.Column(db.String(255))
    stack_details = db.Column(db.String(255))
    available = db.Column(db.Boolean, default=True)

    def __init__(self, full_name, phone_number, stack, stack_details):
        self.full_name = full_name
        self.phone_number = phone_number
        self.stack = stack
        self.stack_details = stack_details

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

        except:
            db.session.rollack()

    @staticmethod
    def get_all():
        return Mentor.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
