from flask.views import MethodView
from flask import request
from flask import session
from flask import Response
from flask import json
from flask import jsonify
from flask import g
from aetam import app
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

        user_id = self.insert_user(request.json['username'], request.json['password'])
        data['status'] = Status.select_from(g.db, user_id)
        data['user'] = User.select_from(g.db, user_id)
        return jsonify(data), 200

    def insert_user(self, username, password):
        pass_sha = self.SHA256_pass(password)
        user_id = User(username, pass_sha).insert_to(g.db)
        Status(user_id, "charname", 0, 0, 0, 0, 0).insert_to(g.db)
        return user_id

    # TODO: sha256
    def SHA256_pass(self, password):
        secret_key = app.config['SECRET_KEY']
        return password
