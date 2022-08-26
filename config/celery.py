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
    # "showroom_buy_car": {
    #     "task": "producer.tasks.showroom_buy_cars",
    #     "schedule": crontab(minute="*/1"),
    # },
    "my_test_task": {
        "task": "src.app.tasks.test_task",
        "schedule": crontab(minute="*/1"),
    },
}
