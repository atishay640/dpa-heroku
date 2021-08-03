import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dpa.settings')

app = Celery('dpa')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'bulk_insert_from_csv': {
        'task' : 'sales.tasks.bulk_insert_from_csv',
        'schedule' : 60*4 # every 4 minutes
    },
    'generate_report_by_store_and_coupon_monthwise': {
        'task' : 'sales.tasks.generate_report_by_store_and_coupon_monthwise',
        'schedule' : 60*3 # every 3 minutes
    },
}

