import os


def fetch_cfg(config_name=os.getenv('FLASK_ENV', 'dev')):
    if config_name.lower() == 'dev':
        return DEV_CONFIG()
    if config_name.lower() == 'pro':
        return PRO_CONFIG()
    if config_name.lower() == 'test':
        return TEST_CONFIG()
