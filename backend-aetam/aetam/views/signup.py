from flask.views import MethodView
from flask import request
from flask import jsonify
from flask import g
from aetam.models import User
from aetam.models import Status
from aetam.views.util import content_type

class SignUpView(MethodView):
    @content_type('application/json')
    def post(self):
        data = {"errors": []}
        if not User.is_valid_username(request.json['username']):
            data['errors'].append('Invalid username')
        if not User.is_valid_password(request.json['password']):
            data['errors'].append('Invalid password')

        if data['errors']:
            return jsonify(data), 400

        data['user'] = User(request.json['username'], request.json['password']).insert_to(g.db)
        data['status'] = Status(data['user']['id'], "charname", 0, 0, 0, 0, 0).insert_to(g.db)
        return jsonify(data), 200

