from flask.views import MethodView
from flask import jsonify, request, g
from aetam.models import User, Status
from aetam.views.util import content_type
from aetam.ai import IpAETaM

class ImageApiView(MethodView):
    @content_type('application/json')
    def post(self):
        data = {"errors": []}
        user = User.select_from(g.db, request.json['ACCESS_KEY'])
        if not user:
            data['errors'].append('Invalid ACCESS_KEY')
        if not request.json['image']:
            data['errors'].append('Not Found image')
        if data['errors']:
            return jsonify(data), 400

        """
        request.json['image'] is binary data
        convert binary to image
        send image to IpAETaM
        data is json object
        """
        self.update_obesity(user.id, obesity)  # Update obesity of DB
        
        return jsonify(data), 200

    def update_obesity(self, user_id, obesity):  # add obesity data
        status = Status.select_from(g.db, user_id)
        obesity += status['obesity']
        status.update_obesity_from(g.db, user_id, obesity)
