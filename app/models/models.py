from . import db


class Mentor(db.Model):
    __tablename__ = "mentor"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    contacts = db.Column(db.String(255))
    stack = db.Column(db.String(255))
    stack_details = db.Column(db.String(255))
    available = db.Column(db.Boolean, default=False)

    def __init__(self, full_name, contacts, stack, stack_details, available):
        self.full_name = full_name
        self.contacts = contacts
        self.stack = stack
        self.stack_details = stack_details
        self.available = available

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
