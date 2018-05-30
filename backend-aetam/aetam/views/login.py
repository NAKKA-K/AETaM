from flask.views import MethodView
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from flask import url_for
from flask import session
from flask import Response
from flask import json


class LoginView(MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        if request.headers['Content-Type'] == 'application/json':
            data = {"errors": []}
            if request.json['username'] == "":
                data['errors'].append('Invalid username')
            if request.json['password'] == "":
                data['errors'].append('Invalid password')

            if data['errors'] == []:
                session['logged_in'] = True
                return Response(
                    status=200,
                    response=json.dumps(data),
                    mimetype='application/json'
                )
            return Response(
                status=400,
                response=json.dumps(data),
                mimetype='application/json'
            )
        else: # TODO: When delelopment is completed, remove the implementation
            if request.form['username'] == "":
                error = 'Invalid username'
            elif request.form['password'] == "":
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                flash('Logged in!')
                return redirect(url_for('index'))

        return render_template('login.html', error=error)

