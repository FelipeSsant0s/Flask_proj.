from ast import main
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)