from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db, User, Milestone, Family, Relationship, Wishlist, Item
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route('/')
def homepage():
    """Homepage"""

    return render_template("homepage.html")

@app.route('/login', methods =['GET', 'POST'])
def view_login_page():
    """Enter login page"""
    if request.method == 'POST':
        email = request.form.get("user_login")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['user_id'] = user.user_id
            print("here I am")
            print(session['user_id'])
            print("Stop!")
            return redirect(url_for('show_welcome_page'))
        print("this does not work!")
        return redirect(url_for('view_login_page')) 
    
    return render_template("login.html")

@app.route('/welcome_page')
def show_welcome_page():
    """user welcome page"""
    
    return render_template("welcome_page.html")

@app.route('/create_account', methods=['GET', 'POST'])
def create_user_account():
    """create user account"""
    if request.method == 'POST':
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        print(full_name,email,password,password2)

        user = User.query.filter_by(email=email).first()
        if user: 
            return redirect(url_for('view_login_page'))

        if password == password2: 
            user = crud.create_user(email, password, full_name)
            print("This is working")
            session["user_id"] = user.user_id
            return redirect(url_for('create_family'))

        elif password != password2:
            flash("Passwords do not match!")
            print("This is also working")
            return redirect(url_for('create_user_account'))

        print("help!")
    return render_template("create_account.html")

@app.route('/create_family')
def create_family():

    return render_template("create_family.html")

@app.route('/complete_family', methods=['GET', 'POST'])
def complete_family():
    """add a family member to your family"""
    if request.method == 'POST':
        print("here I am")
        print(session['user_id'])
        print("Stop!")
          
        user_id = session['user_id']
        full_name = request.form.get("user") 
        birth_date = request.form.get("birth_date")  
        relationship_to_user = request.form.get("relationship_to_user")
        print("************", relationship_to_user)

        relationship = Relationship.query.filter(Relationship.relationship_name == relationship_to_user).first()
        

        image_upload = request.form.get("fileToUpload")
        print("This is working!")

        # Hardcoding family id to be 1 for test purposes
        family_id = 1


        #create the user without an email/password
        #user-obj = crud.create_non_user(full_name)
        #user-obj_id = crud.get_user_by_id(user_obj)
        family_member = crud.create_family_member(family_id,user_id, full_name, birth_date, relationship.relationship_id, image_upload='')
        print("***************************", family_member)
        print("***************************", family_member.family_member_id)
        print("***************************", family_member.family_id)

        # todo: create a wishlist automatically for each family member
        create_wishlist = crud.create_wishlist(family_member.family_member_id, family_member.family_id)
        print('************', create_wishlist)
        
        if family_member:
            return render_template("complete_family.html")

    return render_template("create_family.html")
    


@app.route('/user_profile')
def view_user_profile():
    """view user's profile page"""

    return render_template("user_profile.html")

@app.route('/family_member_profile/<family_id>')
def view_family_profile():
    """view a family member's profile page"""
    
    return render_template("family_profile_page.html")


@app.route('/view_family')
def view_family():
    #query for all family members in our family members table
    #that have the same family id as the current user logged in

    family_id = crud.get_familyid_by_user_id(session['user_id'])
    current_user_family_members = crud.get_family_members(family_id)
  
 
    return render_template ("view_family.html", current_user_family_members=current_user_family_members)

@app.route('/create_wishlist')
def create_wishlist():
    """allows user to create a wishlist"""

    user = crud.get_user_by_user_id(session['user_id'])
    print(user)

    return render_template('login.html')


@app.route('/add_to_wishlist', methods=['GET','POST'])   
def add_to_wishlist():
    """add items to wishlist"""
    #pass a list of family member objects associated with the current user's 
    
    if request.method == 'GET':
        family_id = crud.get_familyid_by_user_id(session['user_id'])
        current_user_family_members = crud.get_family_members(family_id)
       
    return render_template('add_to_wishlist.html', current_user_family_members=current_user_family_members)

@app.route('/item_added_successfully', methods=['POST'])
def item_added_successfully():

    if request.method == 'POST':
        item_name = request.form.get("item")
        print(item_name)
        item_link = request.form.get("link_to_item")
        print(item_link)
        add_to_family_member_wishlist = request.form.get("add_to_family_member_wishlist")
        print(add_to_family_member_wishlist)
        wishlist_items = crud.get_items_by_wishlist_id(add_to_family_member_wishlist)
        print(wishlist_items)
        
        
        if item_name and item_link:
            crud.create_item(add_to_family_member_wishlist, item_name, item_link)

    

    return render_template('item_added_successfully.html')

@app.route('/view_wishlist', methods=['POST'])
def view_wishlist():
    """view items on wishlist"""
    family_id = crud.get_familyid_by_user_id(session['user_id'])
    family_members_wishlist_id = request.form.get("family_members_wishlist_id")
    wishlist_items = crud.get_items_by_wishlist_id(family_members_wishlist_id)
    #item_name = request.form.get()
    print(wishlist_items)
    
   
    return render_template('view_wishlist.html', wishlist_items=wishlist_items)

@app.route('/upcoming_milestones')
def view_upcoming_milestones():
    """allows user to view a list of upcoming events"""
    milestones = crud.get_milestones()
    #TODO add proper templating to make this pretty and not objects 
    return render_template("upcoming_milestones.html", milestones = milestones)

if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug=True)
