from flask import Blueprint
from flask import Flask, jsonify
from flask_restful import Api
from flask_uploads import configure_uploads

from app.config import FlaskConfig
from app.middlewares.login_control_middleware import LoginRequiredMiddleware
from app.resources.upload_data_resource import CSV_UPLOADER, UploadCsv


def create_app():
    app_init = Flask(__name__)
    app_init.config.from_object(FlaskConfig)
    app_init.register_blueprint(api_1_0_blueprint, url_prefix='/api')
    configure_uploads(app_init, (CSV_UPLOADER,))
    app_init.wsgi_app = LoginRequiredMiddleware(app_init.wsgi_app, app_init)
    return app_init


app = create_app()

api_1_0_blueprint = Blueprint('api_1_0', __name__)
api_1_0 = Api(api_1_0_blueprint)

api_1_0.add_resource(UploadCsv, '/upload', endpoint='upload_file')
