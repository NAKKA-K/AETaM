from flask.views import MethodView
from flask import request
from flask import session
from flask import jsonify
from flask import abort
from flask import render_template
from aetam.models import User
from aetam.views.util import content_type

class LoginView(MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        data = {"errors": []}

        for f in request.data:
            print(f)
            print('\n')

        if not User.is_valid_username(request.form['username']):
            data['errors'].append('Invalid username')
        if not User.is_valid_password(request.form['password']):
            data['errors'].append('Invalid password')

        if data['errors']:
            return abort(400)

        session['logged_in'] = True
        return render_template('index.html', error=data['errors'])

