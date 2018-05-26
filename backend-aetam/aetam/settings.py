import os

class Config(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEBUG = False
    TESTING = False
    DATABASE = os.path.join(BASE_DIR, 'aetam.sqlite3')
    HOST = '0.0.0.0'
    PORT = 8000

class ProductConfig(Config):
    pass

class DevelopConfig(Config):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True
