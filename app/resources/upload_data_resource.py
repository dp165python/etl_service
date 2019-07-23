from flask import request, abort

from app.celery_proj.tasks import transfer_data
from app.constants import CSV_UPLOADER, CHUNK_SIZE
from app.constants import PROJECT_SERVICE_URI
from app.resources.base_resourse import BaseResource
from app.schemes.upload_scheme import CsvFileUploadSchema


class UploadCsv(BaseResource):
    project_serice_url = PROJECT_SERVICE_URI

    def post(self):
        filename, project_id, session_id = self._validate_request(request)
        transfer_data.delay(self.project_serice_url.format(uuid=project_id),
                            CHUNK_SIZE, filename, "parser1")
        return 'success', 200

    @staticmethod
    def _validate_request(request_):
        schema = CsvFileUploadSchema().load(request_)
        if schema.errors:
            abort(400, {'message': schema.errors["file"]})
        filename = CSV_UPLOADER.save(schema.data['file'])
        return CSV_UPLOADER.path(filename), schema.data['uuid'], \
               schema.data['session']
