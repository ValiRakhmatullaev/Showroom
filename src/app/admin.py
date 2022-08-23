from django.contrib import admin

from .models import DiscountShowroom, Showroom, ShowroomCar


@admin.register(ShowroomCar)
class ShowroomCarAdmin(admin.ModelAdmin):
    list_display = (
        "producer",
        "price",
        "count",
    )


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    readonly_fields = (
        "added_date",
        "date_updated",
    )
    list_filter = (
        "name",
        "country",
        "is_active",
    )


@admin.register(DiscountShowroom)
class DiscountShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = (
        "added_date",
        "date_updated",
    )
    list_filter = (
        "start_time",
        "end_time",
        "amount_of_discount",
        "is_active",
        "added_date",
        "date_updated",
    )
