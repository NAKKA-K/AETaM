from flask.views import MethodView
from flask import request
from flask import session
from flask import Response
from flask import json
from flask import abort


class LoginView(MethodView):
    def post(self):
        data = {"errors": []}
        if request.headers['Content-Type'] != 'application/json':
            abort(406)
            return

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

