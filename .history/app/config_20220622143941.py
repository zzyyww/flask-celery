import os


class BASE_CONFIG:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DEV_CONFIG(BASE_CONFIG):
    pass


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
