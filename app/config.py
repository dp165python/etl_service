import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
    )


class FlaskConfig:
    UPLOAD_FILES_DEST = os.path.join(BASE_DIR, 'uploads')
    UPLOADS_DEFAULT_DEST = os.path.join(BASE_DIR, 'uploads')
    UPLOAD_FILES_ALLOW = ['csv', ]
    FLASK_AUTH_SERVICE = 'http://127.0.0.1:5000/auth/sid?sid={uuid}'
    FLASK_PORT = 5000
    FLASK_HOST = "127.0.0.1"
