from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from . import dashboard

@dashboard.route("/")
@login_required
def dash_home():
    return render_template('../dashboard/home.html')