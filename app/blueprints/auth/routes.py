from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from app.extensions import mongo
from app.blueprints.auth.models import User


@auth.route("/login", methods=["GET", "POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for("dashboard.dash_home"))
        flash("Invalid username or password", "danger")
    return render_template('auth/login.html', form=form)

@auth.route("/logout")
@login_required
def logout():
    return redirect(url_for("auth.login"))

@auth.route("/register", methods=["GET", "POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        if User.get_by_email(form.email.data):
            flash("Email already exists",'danger')
            return redirect(url_for("auth.login"))
        
        #generate password hash for storage
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

        #insert user into database
        mongo.db.users.insert_one({
            'firstname': form.firstname.data,
            'lastname': form.lastname.data,
            'email': form.email.data,
            'password': hashed_password
        })

        flash("Account created successfully", 'success')
        return redirect(url_for("auth.login"))
    
    return render_template("auth/register.html", form=form)
