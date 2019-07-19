from celery import Celery

from app.constants import BROKER, BACKEND

celery = Celery('app.celery_proj.celery',
                broker=BROKER,
                backend=BACKEND)

celery.autodiscover_tasks(['app.celery_proj.tasks'])
