class Config(object):
    DEBUG = False
    TESTING = False

class ProductConfig(Config):
    pass

class DevelopConfig(Config):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING =True

