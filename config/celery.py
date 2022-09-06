import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # "celery_task": {
    #     "task": "core.celery_tasks.tasks.sample_task",
    #     "schedule": crontab(minute="*/10"),
    # },
    # "showroom_buy_cars": {
    #     "task": "src.producer.tasks.showroom_buy_cars",
    #     "schedule": crontab(minute="*/1"),
    # },
    "buy_car_from_producer": {
        "task": "src.app.tasks.buy_car_from_producer",
        "schedule": crontab(minute="*/1"),
    },
    # "buy_car_from_showroom": {
    #     "task": "src.customer.tasks.buy_car_from_showroom",
    #     "schedule": crontab(minute="*/1"),
    # },
}
