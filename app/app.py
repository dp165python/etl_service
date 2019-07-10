from flask import Flask, jsonify, g
from flask_uploads import configure_uploads

from .middlewares.login_control_middleware import LoginRequiredMiddleware
from .api import api_1_0_blueprint
from .config import FlaskConfig
from .resources import csv_uploader


def custom_exception(error):
    response = jsonify({'message': error.description})
    response.status_code = 400
    return response


def create_app():
    app_init = Flask(__name__)
    app_init.config.from_object(FlaskConfig)
    app_init.register_blueprint(api_1_0_blueprint, url_prefix='/api')
    configure_uploads(app_init, (csv_uploader,))
    app_init.wsgi_app = LoginRequiredMiddleware(app_init.wsgi_app, app_init)
    return app_init


app = create_app()


@app.after_request
def set_auth_header(response):
    auth_cred = g.auth_cred
    response.headers['Authorization'] = auth_cred
    return response
