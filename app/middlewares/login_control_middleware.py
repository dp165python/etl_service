import requests
from flask import abort
from werkzeug.wrappers import Request


class LoginRequiredMiddleware:

    def __init__(self, wsgi_app, app):
        self.app = wsgi_app
        self.auth_url = app.config.get("FLASK_AUTH_SERVICE")

    def __call__(self, environ, start_response):
        request = Request(environ)
        if not self._check_auth(request):
            abort(300, {'message': 'access denied'})
        return self.app(environ, start_response)

    def _check_auth(self, request):
        auth = request.headers.get('Authorization')
        auth_type, credentials = auth.split(' ')
        if auth_type == 'Bearer':
            session = requests.get(self.auth_url.format(
                uuid=credentials))
            if session.status_code != 300:
                return True
            return False
