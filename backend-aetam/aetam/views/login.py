from flask.views import MethodView
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from flask import url_for
from flask import session


class LoginView(MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        error = None
        if request.form['username'] == "":
            error = 'Invalid username'
        elif request.form['password'] == "":
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('Logged in!')
            return redirect(url_for('index'))

        return render_template('login.html', error=error)

