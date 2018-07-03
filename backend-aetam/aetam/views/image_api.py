# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import jsonify, request, g
from aetam.models import User, Status
from aetam.views.util import content_type
from aetam.ai import IpAETaM
from PIL import Image
import io

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

        img_read = request.json['image']
        img_bin = io.BytesIO(img_read)
        pil_img = Image.open(img_bin)
        img = io.BytesIO()
        pil_img.save(img,'PNG')
        image = img.getvalue()
        obesity = IpAETaM(image)
        self.update_obesity(user.id, obesity)
        
        return jsonify(data), 200

<<<<<<< HEAD
    def update_obesity(self, user_id, obesity):  # add obesity data
        status = Status.select_from(g.db, user_id)
        obesity += status['obesity']
        status.update_obesity_from(g.db, user_id, obesity)
=======
    def update_obesity(self, user_id, obesity):
        pass
>>>>>>> master
