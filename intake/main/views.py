from datetime import datetime
from . import main

from flask import request, redirect, render_template, flash
from .forms import IntakeForm
from flask_mail import Message
from intake.main.utils import render_email
from intake import mail

@main.route('/', methods=['GET', 'POST'])
def submit():
    form = IntakeForm()
    if form.validate_on_submit():
        email = render_email(form.data)
        msg = Message("IT Intake Form - {project_name}".format(project_name=form.project_name.data),
                  sender="intake@records.nyc.gov",
                  recipients=["jocastillo@records.nyc.gov", "ppanchal@records.nyc.gov"])
        msg.html = email
        mail.send(msg)
        return redirect('/')
    else:
        for error in form.errors.items():
            flash(error[1][0], category='danger')
    return render_template('main/main.html', form=form)


@main.route('/email', methods=['GET'])
def email():
    return render_template('email/intake_email.html')