class Model(object):
    @classmethod
    def query(cls, db, sql, params):
        cursor = db.cursor()
        ref = cursor.execute(sql, params)
        return ref

    @classmethod
    def execute(cls, db, sql, params):
        cursor = db.cursor()
        cursor.execute(sql, params)
        db.commit()
