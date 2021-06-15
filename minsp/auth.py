from flask import Blueprint, render_template, request, flash, redirect
from flask.helpers import url_for
from .models import insert_Patients, select_Patients
from flask_login import login_user, current_user, logout_user
from .form import LoginForm, SignUpForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already logged in', category='error')
        return redirect(url_for("views.home"))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = select_Patients(form.id.data)
            if user != None and user[2] == form.password.data:
                login_user(user, remember=form.remember.data)
                flash('Login successful.', category='success')
                return redirect(url_for("views.home"))
            else:
                flash('Login Unsuccessful, please check your user-information', category='error')
        else:
            flash('Invalid form', category='error')
    return render_template("login.html", form=form)

@auth.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('Logged out', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if select_Patients(form.cpr_number.data) != None:
                flash('An account is already linked to this CPR-number', category='error')
            else:
                insert_Patients(form.cpr_number.data, form.name.data, form.password.data, form.address.data)
                flash('Account created', category='success')
            return redirect(url_for("auth.login"))
        else:
            flash('Invalid form', category='error')
    return render_template("sign_up.html", form=form)