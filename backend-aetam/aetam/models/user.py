from aetam import app
import re
import secrets

class User(object):
    @classmethod
    def convert_dic(cls, user_array):
        return dict(
            id=user_array[0],
            name=user_array[1],
            access_key=user_array[2]
        )

    @classmethod
    def select_from(cls, db, access_key):
        user = db.execute('select id, name, access_key from Users where access_key=(?)', [access_key]).fetchone()
        return cls.convert_dic(user)

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
    def is_exists_user(cls, db, username):
        cursor = db.cursor()
        data = cursor.execute(
                'select * from Users where name=(?) limit 1',
                [username]).fetchone()
        if data:
            return True
        return False

    def insert_to(self, db):
        cursor = db.cursor()
        access_key = secrets.token_hex(16)
        cursor.execute(
            'insert into Users (name, password, access_key) values (?, ?, ?)',
            [self.username, self.password, access_key]
        )
        db.commit()
        return self.select_from(db, access_key)

    # TODO: sha256
    def SHA256_pass(self, password):
        secret_key = app.config['SECRET_KEY']
        return password

    def __init__(self, username, password):
        self.username = username
        self.password = self.SHA256_pass(password)
