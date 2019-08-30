class Debug(object):
    DEBUG = True
    SECRET_KEY = "Jim"
    SESSION_COOKIE_NAME = "product"


class Test(object):
    TESTING = True
    SECRET_KEY = "Tom"


class Product(object):
    SECRET_KEY = "Sam"
