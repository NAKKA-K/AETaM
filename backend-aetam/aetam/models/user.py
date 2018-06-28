from aetam import app
from aetam.models.model import Model
import re
import os
import base64
import hashlib

class User(Model):
    @classmethod
    def convert_dic_when_signup(cls, user_array):
        if not user_array:
            return None
        return dict(
            id=user_array[0],
            name=user_array[1],
            password=user_array[2],
            access_key=user_array[3],
        )

    @classmethod
    def convert_dic(cls, user_array):
        if not user_array:
            return None
        return dict(
            id=user_array[0],
            name=user_array[1],
            ACCESS_KEY=user_array[2]
        )

    @classmethod
    def select_from(cls, db, access_key):
        user_array = super().query(
            db,
            'select id, name, access_key from Users where access_key=(?)',
            [access_key]).fetchone()
        return cls.convert_dic(user_array)

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
        user_array = super().query(
            db,
            'select * from Users where name=(?) limit 1',
            [username]).fetchone()
        return cls.convert_dic_when_signup(user_array)

    # HACK: Change method name to is_auth_user
    @classmethod
    def is_exists_user_row(cls, db, username, password):
        data = cls.get_exists_user(db, username)
        if data and cls.sha256_pass(password) == data['password']:
            return True
        return False

    @classmethod
    def sha256_pass(cls, password):
        hashing = password + app.config['SECRET_KEY']
        return hashlib.sha256(hashing.encode('utf-8')).hexdigest()

    def insert_to(self, db):
        access_key = self.generate_access_key()
        super().execute(
            db,
            'insert into Users (name, password, access_key) values (?, ?, ?)',
            [self.username, self.password, access_key]
        )
        return self.select_from(db, access_key)

    @classmethod
    def generate_access_key(cls):
        """
        access_key = secrets.token_urlsafe(16)
        Not supported secrets module.
        Therefore the following implementations is substitude.
        """
        return base64.urlsafe_b64encode(os.urandom(16)).decode('ascii') # secure string

    def __init__(self, username, password):
        self.username = username
        self.password = self.sha256_pass(password)
