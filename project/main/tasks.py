from core.celery import app

from .services import get_currency


@app.task
def get_usd_rub_rate():
    get_currency("USD", "RUB")
