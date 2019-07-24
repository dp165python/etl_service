from flask import url_for
import pytest


def test_invalid_get_method(testing_client):
    response = testing_client.get(url_for('api_1_0.upload_file'))
    assert response.status_code == 405


def test_invalid_put_method(testing_client):
    response = testing_client.put(url_for('api_1_0.upload_file'))
    assert response.status_code == 405


def test_invalid_delete_method(testing_client):
    response = testing_client.delete(url_for('api_1_0.upload_file'))
    assert response.status_code == 405


def test_passing_empty_post_request(testing_client, celery_app, celery_worker):
    with pytest.raises(ValueError):
        assert testing_client.post(url_for('api_1_0.upload_file'))