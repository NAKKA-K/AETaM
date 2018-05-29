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
        error = None
        if request.headers['Content-Type'] == 'application/json':
            data = {}
            if request.json['username'] == "":
                data['error'] = 'Invalid username'
            elif request.json['password'] == "":
                data['error'] = 'Invalid password'
            else:
                session['logged_in'] = True
                data['message'] = "Logged in!"
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
        else: # TODO: 開発テスト段階が終われば削除する
            if request.form['username'] == "":
                error = 'Invalid username'
            elif request.form['password'] == "":
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                flash('Logged in!')
                return redirect(url_for('index'))

        return render_template('login.html', error=error)

