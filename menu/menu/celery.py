import os
from celery import Celery
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'menu.settings')

app = Celery('menu')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()