from flask import Blueprint, render_template, request, flash, redirect
from flask.helpers import url_for
from .models import insert_Patients, select_Patients
from . import bcrypt
from flask_login import login_user, current_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpr_number = request.form.get('cpr_number')
        password = request.form.get('password')
        user = select_Patients(cpr_number)
        if user != None and user[2] == password:
            login_user(user, remember=True)
            flash('Login successful.', category='success')
            return redirect(url_for("views.home"))
        else:
            flash('Login Unsuccessful, please check your user-information', category='error')
    if current_user.is_authenticated:
        flash('Already logged in', category='error')
        return redirect(url_for("views.home"))
    else:
        return render_template("login.html")

@auth.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('Logged out', category='success')
    flash('Not logged in', category='error')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        cpr_number = request.form.get('cpr_number')
        name = request.form.get('name')
        password = request.form.get('password')
        address = request.form.get('address')
        if select_Patients(cpr_number) != None:
            flash('An account is already linked to this CPR-number', category='error')
        elif len(cpr_number) < 4:
            flash("CPR-number must be 4 digits or more", category='error')
        else:
            insert_Patients(cpr_number,name, password, address)
            flash('Account created', category='success')
        return redirect(url_for("auth.login"))
    else:
        return render_template("sign_up.html")