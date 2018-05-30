from flask.views import MethodView
from flask import request
from flask import session
from flask import Response
from flask import json
from flask import g
from aetam import app

class SignUpView(MethodView):
    def post(self):
        if request.headers['Content-Type'] == 'application/json':
            data = {"errors": []}
            if request.json['username'] == "":
                data['errors'].append('Invalid username')
            if request.json['password'] == "":
                data['errors'].append('Invalid password')

            if data['errors'] == []:
                user_id = self.insert_user(request.json['username'], request.json['password'])
                data['status'] = self.select_status(user_id)
                data['user'] = self.select_user(user_id)
                return Response(
                    status=200,
                    response=json.dumps(data),
                    mimetype='application/json'
                )
            return Response(
                status=400,
                response=json.dumps(data),
                mimetype='application/json'
            )

    def insert_user(self, username, password):
        pass_sha = self.SHA256_pass(password)
        cursor = g.db.cursor()
        cursor.execute('insert into users (name, password) values (?, ?)', [username, pass_sha])
        user_id = cursor.lastrowid
        cursor.execute('insert into statuses values (?, ?, ?, ?, ?, ?, ?)', [user_id, "charname", 0, 0, 0, 0, 0])
        g.db.commit()
        return user_id

    def select_status(self, user_id):
        status = g.db.execute('select * from statuses where user_id=(?)', [user_id]).fetchone()
        return dict(
            id=status[0],
            name=status[1],
            obesity=status[2],
            serious=status[3],
            hot=status[4],
            strong=status[5],
            kind=status[6]
        )

    def select_user(self, user_id):
        user = g.db.execute('select id, name from users where id=(?)', [user_id]).fetchone()
        return dict(
            id=user[0],
            name=user[1]
        )

    # TODO: sha256
    def SHA256_pass(self, password):
        secret_key = app.config['SECRET_KEY']
        return password
