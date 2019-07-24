import requests
import json

from app.celery_proj.celery import celery
from app.controllers.file_processor_controller import create_chunk


@celery.task
def transfer_data(url_to_send, chnk_size, upload_file, parser_name):
    send_status(url_to_send, status='started')
    data = list(send_chunks(url_to_send, chnk_size, upload_file, parser_name))
    send_status(url_to_send, 'uploaded')

    return data


def send_status(url_to_send, status):
    headers = {'Content-type': 'application/json'}
    return requests.patch(url_to_send, data=json.dumps({'status': status}), headers=headers)


def send_chunks(url_to_send, chunk_size, upload_file, parser_name):
    for chunk in create_chunk(upload_file, parser_name, chunk_size):
        yield send_chunk(url_to_send, chunk)


def send_chunk(url_to_send, chunk):
    data_chunk = json.dumps(dict(data=chunk))
    headers = {'Content-type': 'application/json'}
    requests.post(url_to_send, data=data_chunk, headers=headers)
    return data_chunk
