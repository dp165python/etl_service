import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


class Config:
    UPLOAD_FILES_DEST = os.path.join(BASE_DIR, 'uploads')
    UPLOADS_DEFAULT_DEST = os.path.join(BASE_DIR, 'uploads')
    UPLOAD_FILES_ALLOW = ['csv', ]
    FLASK_PORT = 5000
    FLASK_HOST = "127.0.0.1"


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    SERVER_NAME = "TEST"


class ProductionConfig(Config):
    pass


servers = {
    'testing': TestConfig,
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
}


def runtime_config():
    env = os.environ.get("APP_ENV", 'dev').strip().lower()
    return servers.get(env)
