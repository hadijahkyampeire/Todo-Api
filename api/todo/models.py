import datetime
from api import db


class Todo(db.Model):
    """class for todo table"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    description = db.Column(db.Text)
    day = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """defines representation of the object"""
        return "Todo: {}" .format(self.name)

    def save(self):
        """defines the save method for todo"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """deleting existing todo from db"""
        db.session.delete(self)
        db.session.commit()

    
    