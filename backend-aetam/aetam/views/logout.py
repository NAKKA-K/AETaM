from flask.views import MethodView
from flask import session
from flask import abort

class LogoutView(MethodView):
    def post(self):
        session.pop('logged_in', None)
        abort(200)
