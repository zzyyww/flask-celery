import os


class BASE_CONFIG:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DEV_CONFIG(BASE_CONFIG):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345@127.0.0.1:3306/labeldata"
    REDIS_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_BROKER_URL = REDIS_URL


class PRO_CONFIG(BASE_CONFIG):
    pass


class TEST_CONFIG(BASE_CONFIG):
    pass


def fetch_cfg(config_name=os.getenv('FLASK_ENV', 'dev')):
    if config_name.lower() == 'dev':
        return DEV_CONFIG()
    if config_name.lower() == 'pro':
        return PRO_CONFIG()
    if config_name.lower() == 'test':
        return TEST_CONFIG()