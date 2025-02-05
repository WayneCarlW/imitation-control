from flask import render_template, redirect, url_for, request
from . import auth_bp

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #LOGIN LOGIC
        return redirect(url_for("dashboard.dashboard_home"))
    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    return redirect(url_for("auth.login"))
