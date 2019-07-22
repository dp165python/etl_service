import os

from flask_uploads import UploadSet

BROKER = "pyamqp://{user}:{passw}@{broker}:{port}".format(user=os.environ.get("BROKER_USER", "guest"),
                                                          passw=os.environ.get("BROKER_PWD", "guest"),
                                                          broker=os.environ.get("BROKER", "localhost"),
                                                          port=os.environ.get("BROKER_POT", "5672"))
BACKEND = "amqp://{user}:{passw}@{broker}:{port}".format(user=os.environ.get("BROKER_USER", "guest"),
                                                         passw=os.environ.get("BROKER_PWD", "guest"),
                                                         broker=os.environ.get("BROKER", "localhost"),
                                                         port=os.environ.get("BROKER_POT", "5672"))
LOGGED_IN = 200

DIR = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "parsers"))

CURRENCY = {
    '₴': 'UAH',
    '$': 'USD',
    '€': 'EUR'
}

CSV_UPLOADER = UploadSet('CsvUploader')
CHUNK_SIZE = 50
