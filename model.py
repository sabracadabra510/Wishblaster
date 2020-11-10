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


class Family(db.Model):
   """Family member's table"""
    __tablename__ = "family"

    family_id = db.Column(db.Integer,
                autoincrement = True,
                primary_key = True)

    user_id = db.Colum(db.Integer, db.ForeignKey('users.user_id'))
    full_name = db.Column(db.String)
    birth_date = db.Column(db.Datetime)
    relationship_to_user = db.Column(db.Integer)
    image_upload =db.Column(db.String)

    def __repr__(self):
        return f'<Family family_id ={self.family_id} full_name={self.full_name}>'