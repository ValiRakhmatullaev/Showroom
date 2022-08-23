from django.contrib import admin

# Register your models here.
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    readonly_fields = (
        "added_date",
        "date_updated",
    )
    list_filter = (
        "model",
        "year",
        "color",
        "engine",
        "body_type",
    )
