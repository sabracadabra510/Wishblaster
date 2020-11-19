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
            print("This works!")
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

@app.route('/create_family', methods=['GET', 'POST'])
def create_family():
    """add a family member to your family"""
    if request.method == 'POST':
        full_name = request.form.get("user") 
        birth_date = request.form.get("birth_date")  
        relationship_to_user = request.form.get("relationship_to_user")  
        image_upload = request.form.get("fileToUpload")
        print("This is working!")
        family_member = crud.create_family_member(full_name, birth_date, relationship_to_user, image_upload)
        
        if family_member:
            return redirect(url_for('complete_create_family'))

    return render_template("create_family.html")

@app.route('/complete_family')
def complete_create_family():
    """complete adding members to family"""

    return render_template('complete_family.html')

@app.route('/user_profile')
def view_user_profile():
    """view user's profile page"""

    return render_template("user_profile.html")

@app.route('/family_member_profile')
def view_family_profile():
    """view a family member's profile page"""

    return render_template("family_profile_page.html")

@app.route('/search_for_user')
def search_for_user():
    """search for a user"""

    return render_template("search_users.html")

@app.route('/add_to_wishlist')
def add_to_wishlist():
    """add items to wishlist"""

    return render_template('add_to_wishlist.html')

@app.route('/upcoming_milestones')
def view_upcoming_milestones():
    """allows user to view a list of upcoming events"""
    milestones = crud.get_milestones()

    return render_template("upcoming_milestones.html", milestones = milestones)

if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug=True)
