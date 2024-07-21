import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# beat tasks

app.conf.beat_schedule = {
    "deposit_daily_money_add": {
        "task": "main.tasks.get_usd_rub_rate",
        "schedule": crontab(minute="*/1"),
    },
}
