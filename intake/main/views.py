from . import main

from flask import request, redirect, render_template, flash
from .forms import IntakeForm

@main.route('/', methods=('GET', 'POST'))
def submit():
    form = IntakeForm()
    if form.validate_on_submit():
        print(form.data)
        return redirect('/')
    else:
        for error in form.errors.items():
            flash(error[1][0], category='danger')
    return render_template('main/main.html', form=form)