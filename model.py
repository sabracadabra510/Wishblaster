"""Models for Wishblaster."""

from flask_sqlalchemy import flask_sqlalchemy


db = SQLAlchemy()

#creating classes

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    full_name = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'