from flask import url_for


def test_invalid_get_method(testing_client):
    response = testing_client.get(url_for('api_1_0.upload_file'))
    assert response.status_code == 405
