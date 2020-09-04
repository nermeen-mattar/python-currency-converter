
import os
from celery import Celery
# import django
# django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency.settings')

celery_app = Celery('currency', broker= 'redis://localhost:6379', include=["currency.tasks"])
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()