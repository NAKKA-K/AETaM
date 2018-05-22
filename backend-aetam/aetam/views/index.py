from flask import Flask
from flask.views import MethodView

class IndexView(MethodView):
    def get(self):
        return 'Hello, world!'

