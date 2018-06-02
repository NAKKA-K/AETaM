from flask.views import MethodView
from flask import request
from flask import session
from flask import Response
from flask import json
from flask import jsonify
from flask import abort
from aetam.views.util import content_type

class LoginView(MethodView):
    @content_type('application/json')
    def post(self):
        data = {"errors": []}

        if request.json['username'] == "":
            data['errors'].append('Invalid username')
        if request.json['password'] == "":
            data['errors'].append('Invalid password')
        if data['errors'] == []:
            session['logged_in'] = True
            return jsonify(data)

        return jsonify(data), 400
