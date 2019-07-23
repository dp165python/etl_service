import pytest
from app.app import create_app
from app.constants import BROKER, BACKEND


@pytest.fixture(scope='module')
def testing_client():
    flask_app = create_app()
    test_client = flask_app.test_client()

    context = flask_app.app_context()
    context.push()

    yield test_client

    context.pop()


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': BROKER,
        'result_backend': BACKEND
    }