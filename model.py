"""Models for Wishblaster."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#creating classes

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    full_name = db.Column(db.String)
    email = db.Column(db.String, unique = True, nullable=True)
    password = db.Column(db.String, nullable=True)



    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Family(db.Model):
    """Family table"""
    __tablename__ = "family"

    family_id = db.Column(db.Integer,
                autoincrement = True,
                primary_key = True)
    surname = db.Column(db.String)



class FamilyMember(db.Model):
    """Family members table."""
    __tablename__ = "family_members"

    family_member_id = db.Column(db.Integer,
                autoincrement = True,
                primary_key = True)

    family_id = db.Column(db.Integer, db.ForeignKey('family.family_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    full_name = db.Column(db.String)
    birth_date = db.Column(db.DateTime)
    relationship_to_user = db.Column(db.Integer, db.ForeignKey('relationships.relationship_id'))

    relationship_model = db.relationship("Relationship")
    image_upload =db.Column(db.String)

    members_wishlist = db.relationship("Wishlist")



    def __repr__(self):
        return f'<FamilyMember family_member_id={self.family_member_id} family_id ={self.family_id} full_name={self.full_name}>'
               

class Milestone(db.Model):
    """Family Milestones table."""
    __tablename__ = "milestones"

    milestone_id = db.Column(db.Integer,
                             autoincrement = True,
                             primary_key = True)
                            
    milestone_name = db.Column(db.String)
    milestone_date = db.Column(db.DateTime)
    family_id = db.Integer, db.ForeignKey('family.family_id')

    def __repr__(self):
        return f'<Milestones milestone_id ={self.milestone_id} milestone_name={self.milestone_name}>'

class Relationship(db.Model):
    """Relationships table."""
    __tablename__ = "relationships"

    relationship_id = db.Column(db.Integer,
                                autoincrement=True,
                                primary_key=True)
    relationship_name = db.Column(db.String)

    def __repr__(self):
        return f'<Relationship relationship_id ={self.relationship_id} relationship_name={self.relationship_name}>'

class Wishlist(db.Model):
    """Wishlists table"""

    __tablename__ = "wishlists"

    wishlist_id = db.Column(db.Integer,
                            primary_key=True,
                            autoincrement=True)
    family_member_id = db.Column(db.Integer, db.ForeignKey('family_members.family_member_id'))
    family_id = db.Column(db.Integer, db.ForeignKey('family.family_id'))

    def __repr__(self):
        return f'<Wishlists wishlist_id ={self.wishlist_id} family_id ={self.family_id} family_member_id ={self.family_member_id}>'

class Item(db.Model):
    """Items on wishlist table"""

    __tablename__ = "items"

    item_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlists.wishlist_id'))
    item_name = db.Column(db.String)
    item_link = db.Column(db.String)

                                
    def __repr__(self):
        return f'<Items item_id ={self.item_id} item_name={self.item_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///wishblaster', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_DATABASE_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connect to Wishblaster db!')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)