from flask import Blueprint
from flask import Flask, abort
from flask_uploads import configure_uploads

from app.api import Api
from app.config import runtime_config
from app.resources.upload_data_resource import CSV_UPLOADER, UploadCsv


def create_app():
    app_init = Flask(__name__)
    app_init.config.from_object(runtime_config())
    configure_uploads(app_init, (CSV_UPLOADER,))

    api_1_0_blueprint = Blueprint('api_1_0', __name__)
    api_1_0 = Api(api_1_0_blueprint)
    api_1_0.add_resource(UploadCsv, '/files', endpoint='upload_file')
    app_init.register_blueprint(api_1_0_blueprint, url_prefix='/api')

    return app_init


app = create_app()