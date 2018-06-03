class User(object):
    @classmethod
    def convert_dic(cls, user_array):
        return dict(
            id=user_array[0],
            name=user_array[1]
        )
    @classmethod
    def select_from(cls, db, user_id):
        user = db.execute('select id, name from users where id=(?)', [user_id]).fetchone()
        return cls.convert_dic(user)

    @classmethod
    def is_valid_username(cls, username):
        if username != '':
            return True
        return False

    @classmethod
    def is_valid_password(cls, password):
        if password != '':
            return True
        return False

    def insert_to(self, db):
        cursor = db.cursor()
        cursor.execute('insert into users (name, password) values (?, ?)', [self.username, self.password])
        db.commit()
        return cursor.lastrowid

    def __init__(self, username, password):
        self.username = username
        self.password = password
