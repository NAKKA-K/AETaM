from flask.views import MethodView
from flask import jsonify, request, g
from aetam.models import User, Status
from aetam.views.util import content_type
from aetam.ai import LaAETaM

class WordApiView(MethodView):
    @content_type('application/json')
    def post(self):
        data = {"errors": []}
        user = User.select_from(g.db, request.json['ACCESS_KEY'])
        if not user:
            data['errors'].append('Invalid ACCESS_KEY')
        if not request.json['word']:
            data['errors'].append('Not Found word')
        if data['errors']:
            return jsonify(data), 400

        personality_json = LaAETaM(request.json['word']).execute()
        update_status(user['id'], personality_json)
        print(Status.select_from(g.db, user_id))
        return jsonify(data), 200

    def update_status(self, user_id, personality_json):
        status = Status.select_from(g.db, user_id)
        print(status)
        personality_json['serious'] += status['serious']
        personality_json['hot'] += status['hot']
        personality_json['strong'] += status['strong']
        personality_json['kind'] += status['kind']
        Status.update_personal_from(g.db, user_id, personality_json)

