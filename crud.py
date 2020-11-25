from model import db, User, Family,FamilyMember, Milestone, Relationship, Wishlist, Item, connect_to_db

def create_user(email, password, full_name):
    """Create and return a new user."""

    user = User(email=email, password=password, full_name=full_name)


    db.session.add(user)
    db.session.commit()

    return user

def create_non_user(full_name):
    """Creates a user who can't login i.e. 4 year old niece"""

    user = User(full_name)

    return user


def create_family(surname):
    """Create a family and return the family primary id."""

    family = Family(surname=surname)
    db.session.add(family)
    db.session.commit()

    return family


def create_family_member(family_id, user_id, full_name, birth_date, relationship_to_user, image_upload):
    
    family_member = FamilyMember(family_id=family_id, user_id=user_id, full_name=full_name, birth_date=birth_date, relationship_to_user=relationship_to_user, image_upload=image_upload)
    
    db.session.add(family_member)
    db.session.commit()

    return family_member

def create_milestone(milestone_name,milestone_date, family_id):
 
    milestone = Milestone(milestone_name = milestone_name, milestone_date=milestone_date, family_id=family_id)

    db.session.add(milestone)
    db.session.commit()

    return milestone

def get_milestones():

    return Milestone.query.all()

def create_relationship(relationship_name):

    relationship = Relationship(relationship_name=relationship_name)

    db.session.add(relationship)
    db.session.commit()

    return relationship

def create_wishlist(family_member_id, family_id):

    wishlist = Wishlist(family_member_id=family_member_id, family_id=family_id)

    db.session.add(wishlist)
    db.session.commit()

    return wishlist

def get_wishlist():

    return Wishlist.query.all()

def get_user_by_user_id(user_id):

    return User.query.filter(User.user_id==user_id).first()

def create_item(wishlist_id, item_name, item_link):

    item = Item(wishlist_id = wishlist_id, item_name = item_name, item_link= item_link)

    db.session.add(item)
    db.session.commit()

    return item 

def get_familyid_by_user_id(user_id):

    current_user = FamilyMember.query.filter(FamilyMember.user_id==user_id).first()

    return current_user.family_id


def get_family_members(family_id):

    return FamilyMember.query.filter(FamilyMember.family_id==family_id).all() 


if __name__ == '__main__':
    from server import app
    connect_to_db(app)