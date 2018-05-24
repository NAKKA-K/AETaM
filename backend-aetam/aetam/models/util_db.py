from flask import g
from aetam import app
from contextlib import closing

class UtilDB(object):
    def init(self):
        with closing(self.connect()) as db:
            with app.open_resource('schema.sql') as :
                pass

    def connect(self):
        return sqlite3.connect(app.config['DATABASE'])

    @app.before_request
    def before_request(self):
        g.db = self.connect

    @app.after_request
    def after_request(self, response):
        g.db.close()
        return response
