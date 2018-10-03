from flask import Markup, render_template
from datetime import datetime

def render_email(data):
    today = str(datetime.now().today().date())
    return render_template('email/intake_email.html', today=today, form=data)
