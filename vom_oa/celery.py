import os
import django
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','vom_oa.settings')
django.setup()

app=Celery('vom_oa')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()