from flask import render_template, flash
from app import db, app
from app.forms import RegistrationForm
from app.models import User


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
    return render_template('register.html', title='Register',
                           form=form)
