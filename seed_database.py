import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server
from faker import Faker 

fake = Faker()

os.system('dropdb wishblaster')
os.system('createdb wishblaster')
model.connect_to_db(server.app)
model.db.create_all()

users = []

for i in range(10):
    user = crud.create_user(fake.email(), 'password', fake.name())
    users.append(user)


for user in users:
    print(user.full_name)

relationships ={}

for relationship_name in ['self','son','daughter' ,'brother', 'sister', 'mom','dad', 'cousin', 'aunt','uncle', 'grandma', 'grandpa', 'niece', 'nephew', 'sister in law', 'brother in law']:
    relationship = crud.create_relationship(relationship_name)
    relationships[relationship_name] = relationship

family_members = []
for user in users: 
    family_member = crud.create_family_member(user.user_id, user.full_name, fake.date_of_birth(), relationships['self'].relationship_id, '')
    family_members.append(family_member)
for family_member in family_members:
    print(family_member.full_name, family_member.birth_date, family_member.relationship_to_user)


milestones = []

for milestone in milestones:
    #TODO check to see how to bring in fake date from Faker 
    milestone = crud.create_milestone(milestone_name, user.user_id, fake.)

wishlists = []

for wishlist in wishlists:
    wishlist = crud.create_wishlist(wishlist_name, family.family_id)
    wishlist.append(wishlist)


items = []

for item in items:
    #TODO check to see if I can bring in fake items from Faker 
    item = crud.create_item(wishlist.wishlist_id, item_name, item_link)
    items.append(item)
