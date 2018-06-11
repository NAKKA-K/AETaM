from aetam import app
import re
import os
import base64
import hashlib

class User(object):
    @classmethod
    def convert_dic(cls, user_array):
        return dict(
            id=user_array[0],
            name=user_array[1],
            ACCESS_KEY=user_array[2]
        )

    @classmethod
    def select_from(cls, db, access_key):
        user = db.execute('select id, name, access_key from Users where access_key=(?)', [access_key]).fetchone()
        if user:
            return cls.convert_dic(user)
        return None

    @classmethod
    def is_valid_username(cls, username):
        match = re.match(r"^.{4,16}$", username)
        if match:
            return True
        return False

    @classmethod
    def is_valid_password(cls, password):
        match = re.match(r"^.{8,16}$", password)
        if match:
            return True
        return False

    @classmethod
    def get_exists_user(cls, db, username):
        cursor = db.cursor()
        data = cursor.execute(
            'select * from Users where name=(?) limit 1',
            [username]).fetchone()
        if not data:
            return None
        return dict(
            id=data[0],
            name=data[1],
            password=data[2],
            access_key=data[3],
        )

    # HACK: Change method name to is_auth_user
    @classmethod
    def is_exists_user_row(cls, db, username, password):
        cursor = db.cursor()
        data = cls.get_exists_user(db, username)
        if data and cls.sha256_pass(password) == data['password']:
            return True
        return False

    @classmethod
    def sha256_pass(cls, password):
        hashing = password + app.config['SECRET_KEY']
        return hashlib.sha256(hashing.encode('utf-8')).hexdigest()

    def insert_to(self, db):
        """
        access_key = secrets.token_urlsafe(16)
        Not supported secrets module.
        Therefore the following implementations is substitude.
        """
        cursor = db.cursor()
        access_key = base64.urlsafe_b64encode(os.urandom(16)).decode('ascii') # secure string
        cursor.execute(
            'insert into Users (name, password, access_key) values (?, ?, ?)',
            [self.username, self.password, access_key]
        )
        db.commit()
        return self.select_from(db, access_key)


    def __init__(self, username, password):
        self.username = username
        self.password = self.sha256_pass(password)
