from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import insert_result, select_all_data
import matplotlib.pyplot as plt
import mpld3
from pathlib import Path
from os.path import join
from .form import InsertResultForm


results = Blueprint('results', __name__)
path = join(join(Path(__file__).parent, "static"), "plot.html")


@results.route('/HbA1c_results', methods=['GET', 'POST'])
@login_required
def HbA1c_results():
    result = select_all_data(current_user[0])
    if result == None:
        flash("No data available for this user", category='error')
        return redirect(url_for("views.home"))
    else:
        a = []
        b = []

        for e in result:
            a.append(e[0])
            b.append(e[1])
        fig = plt.figure()
        plt.plot_date(b, a, 'b-')
        mpld3.save_html(fig, path)
        flash("Plot successful", category='success')

        return render_template("HbA1c_results.html", path=path)

@results.route('/insert_results', methods=['GET', 'POST'])
@login_required
def insert_results():
    form = InsertResultForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.result.data > 15 or form.result.data < 0:
                flash('Result outside expected range', category='error')
            else:
                insert_result(form.result.data, form.date_of_test.data, current_user[0])
                flash('Test result inserted into database', category='success')
                return redirect(url_for('views.home'))
        else:
            flash('Invalid form', category='error')
    return render_template('insert_results.html', form=form)

