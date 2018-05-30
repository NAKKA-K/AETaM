import os
import sqlite3
from flask import g
from aetam import app
from contextlib import closing

# Create db file
# The schema is stored in the migratinos directory
def init():
    with closing(connect()) as db:
        schema_file = os.path.join(app.config['BASE_DIR'], 'aetam/migrations/schema.sql')
        with app.open_resource(schema_file) as sql:
            db.cursor().executescript(sql.read().decode('utf-8'))
        db.commit()

# Return a connection DB
def connect():
    return sqlite3.connect(app.config['DATABASE'])

# Set db connection to g
# Call request before view
@app.before_request
def before_request():
    g.db = connect()

# Close db connection
# Call request after view
@app.after_request
def after_request(response):
    g.db.close()
    return response
