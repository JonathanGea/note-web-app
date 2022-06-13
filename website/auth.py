import email
import re
from flask import Blueprint, render_template, request, flash


auth = Blueprint ('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p> logout </p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4 :
            flash('email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2 :
            flash('first name must be grater 1 characters.', category='error')
        elif len(password1) < 7 :
            flash('password to short must be at least 7 chareacters.', category='error')
        else :
            flash('account created', category='success')

    return render_template("sign_up.html")