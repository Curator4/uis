from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import select_all_data
import matplotlib.pyplot as plt
import mpld3
from pathlib import Path
from os.path import join


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
