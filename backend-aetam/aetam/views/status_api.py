from flask.views import MethodView
from flask import jsonify, request, g
from aetam.models import User, Status
from aetam.views.util import content_type

class StatusApiView(MethodView):
    @content_type('application/json')
    def get(self):
        data = {"errors": []}
        user = User.select_from(g.db, request.json['ACCESS_KEY'])
        if not user:
            data['errors'].append('Invalid access_key')
            return jsonify(data), 400

        data['status'] = Status.select_from(g.db, user['id'])
        return jsonify(data), 200
