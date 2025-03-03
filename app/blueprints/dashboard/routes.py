from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_required, current_user
from . import dashboard


@dashboard.route("/dash")
@login_required
def dash():
    return render_template('/dashboard/home.html', email=current_user.email)