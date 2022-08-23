from django.contrib.auth.models import AbstractUser
from django.db import models


class ShowroomUser(AbstractUser):
    is_producer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_showroom = models.BooleanField(default=False)

    def __str__(self):
        template = "{0.username}"
        return template.format(self)
