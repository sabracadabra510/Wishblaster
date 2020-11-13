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

@app.route('/login')
def view_login_page():
    """Enter login page"""
    user_name = request.form.get("user_login")
    password = request.form.get("password")

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
    """add a family member to your family"""

    return render_template("create_family.html")

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

    return render_template("upcoming_milstones.html")

if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug=True)
