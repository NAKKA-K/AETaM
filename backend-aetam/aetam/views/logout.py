from flask.views import MethodView
from flask import session
from flask import abort
from flask import jsonify

class LogoutView(MethodView):
    def post(self):
        data = {'errors': []}
        session.pop('logged_in', None)
        return jsonify(data), 200
