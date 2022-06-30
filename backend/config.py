

class Config(object):
    # all of the classes below is going to inherit these variables
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    CORS_HEADERS = 'Content-Type'
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    # interactive debugger will be shown for unhandled exceptions
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    CORS_HEADERS = 'Content-Type'
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    CORS_HEADERS = 'Content-Type'
    SESSION_COOKIE_SECURE = False


