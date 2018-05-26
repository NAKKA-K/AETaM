import os
import sqlite3
from flask import g
from aetam import app
from contextlib import closing

# DBファイルの作成を行う
# schemaはmigrationsディレクトリに格納
def init():
    with closing(connect()) as db:
        schema_file = os.path.join(app.config['BASE_DIR'], 'aetam/migrations/schema.sql')
        with app.open_resource(schema_file) as sql:
            db.cursor().executescript(sql.read().decode('utf-8'))
        db.commit()

# DBへの接続変数を返す
def connect():
    return sqlite3.connect(app.config['DATABASE'])

# DBへの接続変数をgという環境変数に格納する
# appのリクエスト直前に呼ばれる
@app.before_request
def before_request():
    g.db = connect()

# DBの接続変数を閉じる
# appのリクエスト終了時に呼ばれる
@app.after_request
def after_request(response):
    g.db.close()
    return response
