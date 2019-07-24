from flask_restful import Resource

from app.controllers.authentication_controller import authentication


class BaseResource(Resource):
    # method_decorators = [authentication]
    pass
